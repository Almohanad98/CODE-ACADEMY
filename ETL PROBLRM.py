import pandas as pd
from sqlalchemy import create_engine
import pymysql
import unicodedata

# Load CSV files
df1 = pd.read_csv("C:/Users/USER PC/Downloads/store_sales_1.csv")
df2 = pd.read_csv("C:/Users/USER PC/Downloads/store_sales_2.csv")
df3 = pd.read_csv("C:/Users/USER PC/Downloads/store_sales_3.csv")

# Data cleaning function
def fill_missing_with_mean(df, df_name="DataFrame"):
    df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
    df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')

    qty_mean = df['Qty'].mean()
    price_mean = df['Unit_Price'].mean()

    df['Qty'] = df['Qty'].fillna(qty_mean)
    df['Unit_Price'] = df['Unit_Price'].fillna(price_mean)
    df['CustomerID'] = df['CustomerID'].fillna('UNKNOWN')
    df['CurrencyType'] = df['CurrencyType'].fillna('OMR')

    # Normalize currency type
    df['CurrencyType'] = df['CurrencyType'].apply(
        lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', 'ignore').decode('utf-8').upper()
    )
    df['StoreID'] = df['StoreID'].apply(lambda x: 
    unicodedata.normalize('NFKD', str(x))  
    .encode('ascii', 'ignore').decode('utf-8')  
    .upper()  
    .replace('-', '_') 
    .strip()  
)

        
    # Convert USD to OMR
    df.loc[df['CurrencyType'] == 'USD', 'Unit_Price'] *= 0.39
    df.loc[df['CurrencyType'] == 'USD', 'CurrencyType'] = 'OMR'

    print(f"{df_name} - Cleaned. Filled Qty mean: {qty_mean:.2f}, Unit_Price mean: {price_mean:.2f}")
    return df


# Clean the data
df1_clean = fill_missing_with_mean(df1, "df1")
df2_clean = fill_missing_with_mean(df2, "df2")
df3_clean = fill_missing_with_mean(df3, "df3")

print(df1)

print("\nAfter cleaning:")
print("df1 missing values:\n", df1_clean[['Qty', 'Unit_Price']].isnull().sum())
print("df2 missing values:\n", df2_clean[['Qty', 'Unit_Price']].isnull().sum())
print("df3 missing values:\n", df3_clean[['Qty', 'Unit_Price']].isnull().sum())

print("df1 columns:", df1.columns)
print("df2 columns:", df2.columns)
print("df3 columns:", df3.columns)



# Merge data
df_all = pd.concat([df1_clean, df2_clean, df3_clean], ignore_index=True)

df_all['SaleDate'] = pd.to_datetime(df_all['SaleDate'], errors='coerce').dt.date;


print(df_all['StoreID'].unique())
print()
print(df_all['CurrencyType'].unique())


connection = pymysql.connect(
    user='root',
    password='Al@mohanad98',
    host='127.0.0.1',
    port=3306,
    database='StoreSalesDB',
    autocommit=True
)

try:
    with connection.cursor() as cursor:
        # Check DB version
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("Database version:", version[0])

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS SalesData (
                SaleID INT AUTO_INCREMENT PRIMARY KEY,
                ProductName VARCHAR(255),
                Qty DECIMAL(10,2),
                Unit_Price DECIMAL(10,2),
                SaleDate DATE,
                CurrencyType VARCHAR(10),
                CustomerID VARCHAR(100),
                StoreID VARCHAR(100)
            )
        """)

        # Insert all rows from df_all
        insert_query = """
            INSERT INTO SalesData (ProductName, Qty, Unit_Price, SaleDate, CurrencyType, CustomerID, StoreID)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Loop through df_all and insert rows
        for _, row in df_all.iterrows():
            cursor.execute(insert_query, (
                row['ProductName'],
                row['Qty'],
                row['Unit_Price'],
                row['SaleDate'],
                row['CurrencyType'],
                row['CustomerID'],
                row['StoreID']
            ))

    print(" Data successfully loaded into MySQL table 'SalesData'.")

finally:
    connection.close()