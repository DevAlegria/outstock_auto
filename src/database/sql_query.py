class SifacPOS:
  def __init__(self, cursor):
    self.cursor = cursor

  def getLatestSales(self, timeframeHours = 1):
    query = f'''SELECT d.strReferencia, d.strDescripcion, p.intId, p.dtFecha_Compra, d.intIdInventario, d.intIdPOS
      FROM tblPOS p
      INNER JOIN tblDetallePOS d
      ON p.intId = d.intIdPOS
      WHERE p.dtFecha_Compra >= DATEADD(HOUR, -{timeframeHours}, GETDATE())
      ORDER BY p.dtFecha_Compra DESC'''

    self.cursor.execute(query)
    return self.cursor.fetchall()
  
  def getProductDetails(self, reference):
    query = f"""SELECT strReferencia, strCodigo, strDescripcion, intCantidadMinimaAviso, intCantidad, strIdProveedor
    FROM tblInventario where strReferencia = '{reference}'"""
    self.cursor.execute(query)
    return self.cursor.fetchone()