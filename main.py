from src.database.db_config import getDbConnection
from src.database.sql_query import SifacPOS

def main():
    conn = getDbConnection()
    cursor = conn.cursor()
    sifacPOS = SifacPOS(cursor)

    latestSales = sifacPOS.getLatestSales()
    print("Latest Sales:")
    for sale in latestSales:
        print(sale)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()