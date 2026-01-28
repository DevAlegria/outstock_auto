from db_config import get_db_connection

getOutStock = '''SELECT
	d.strReferencia,
	d.strDescripcion, 
	p.intId,
    p.dtFecha_Compra,
    d.intIdInventario,
    d.intIdPOS
FROM tblPOS p
INNER JOIN tblDetallePOS d
    ON p.intId = d.intIdPOS
WHERE p.dtFecha_Compra >= DATEADD(HOUR, -1, GETDATE())
ORDER BY p.dtFecha_Compra DESC'''

def gettProduct(reference):
    return f"""SELECT
	strReferencia,
	strCodigo,
	strDescripcion,
	intCantidadMinimaAviso,
	intCantidad,
	strIdProveedor
    FROM tblInventario where strReferencia = '{reference}'"""

listName = 'Agotados hoy'
connection = get_db_connection()
cursor = connection.cursor()
cursor.execute(getOutStock)

rows = cursor.fetchall()
with open(f'{listName}.txt', 'w', encoding='utf-8') as list:
    for row in rows:
        reference = row.strReferencia

        cursor.execute(gettProduct(reference)) 
        product_data = cursor.fetchone()

        list.write(f"Referencia: {product_data.strReferencia} Descripcion: {product_data.strDescripcion} Cantidad: {product_data.intCantidad}\n")

cursor.close()
connection.close()