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

getProduct = """SELECT
	strReferencia,
	strCodigo,
	strDescripcion,
	intCantidadMinimaAviso,
	intCantidad,
	strIdProveedor
FROM tblInventario where strReferencia = '9903907014068'"""

connection = get_db_connection()
cursor = connection.cursor()
cursor.execute(getOutStock)

for row in cursor:
    reference = row.strReferencia
    product = connection.cursor()
    product.execute(getProduct).fetchone()
    print(product)
    print(row)