from src.database.db_config import getDbConnection
from src.database.sql_query import SifacPOS
from src.writer import ReportWriter
from src.product import Product

def main():
    conn = getDbConnection()
    cursor = conn.cursor()
    sifacPOS = SifacPOS(cursor)
    reporter = ReportWriter('sales_report', ['Referencia','Codigo','Descripcion', 'Cantidad'])
    listOutStock = {}

    latestSales = sifacPOS.getLatestSales()

    for sale in latestSales:
        reference = sale.strReferencia
        if listOutStock.get(reference):
            continue

        productDetails = sifacPOS.getProductDetails(reference)
        if productDetails is None:
            continue

        if productDetails.intCantidad <= 0 or productDetails.intCantidad <= productDetails.intCantidadMinimaAviso:
            product = Product(reference, productDetails.strCodigo, productDetails.strDescripcion, productDetails.intCantidad)
            listOutStock[reference] = product

    for ref, obj in listOutStock.items():
        row = [obj.reference, obj.code, obj.description, obj.quantity]
        reporter.append_row(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()