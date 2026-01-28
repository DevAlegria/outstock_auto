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
    return """SELECT
	strReferencia,
	strCodigo,
	strDescripcion,
	intCantidadMinimaAviso,
	intCantidad,
	strIdProveedor
    FROM tblInventario where strReferencia = '{reference}'"""

connection = get_db_connection()
cursor = connection.cursor()
cursor.execute(getOutStock)

rows = cursor.fetchall()

for row in rows:
    reference = row.strReferencia
    
    cursor.execute(gettProduct(reference)) 
    product_data = cursor.fetchone()
    
    print("Datos del Producto:", product_data)

cursor.close()
connection.close()