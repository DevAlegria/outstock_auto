from db_config import get_db_connection
import datetime

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

listName = 'reporte_agotados'
connection = get_db_connection()
cursor = connection.cursor()
cursor.execute(getOutStock)

rows = cursor.fetchall()
fecha_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(f'{listName}.md', 'w', encoding='utf-8') as list_file:
    list_file.write(f"# Reporte de Agotados\n")
    list_file.write(f"**Fecha:** {fecha_str}\n\n")
    list_file.write("| Referencia | Código | Descripción | Cantidad |\n")
    list_file.write("| :--- | :--- | :--- | :--- |\n")

    for row in rows:
        reference = row.strReferencia
        cursor.execute(gettProduct(reference)) 
        product_data = cursor.fetchone()

        if product_data:
            ref = product_data.strReferencia
            cod = product_data.strCodigo
            desc = product_data.strDescripcion
            cant = f"{product_data.intCantidad:.2f}"

            list_file.write(f"| {ref} | {cod} | {desc} | {cant} |\n")

cursor.close()
connection.close()