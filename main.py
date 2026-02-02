from src.database.db_config import getDbConnection
from src.database.sql_query import SifacPOS
from src.writer import ReportWriter

def main():
    conn = getDbConnection()
    cursor = conn.cursor()
    sifacPOS = SifacPOS(cursor)
    reporter = ReportWriter('sales_report', ['Reference','Description'])

    latestSales = sifacPOS.getLatestSales()

    for sale in latestSales:
        reference = sale.strReferencia
        productDetails = sifacPOS.getProductDetails(reference)

        if productDetails:
            row = [
                productDetails.strReferencia,
                productDetails.strDescripcion
            ]
            reporter.append_row(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()