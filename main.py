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

cursor = get_db_connection().cursor()
cursor.execute(getOutStock)

for row in cursor:
    print(row)