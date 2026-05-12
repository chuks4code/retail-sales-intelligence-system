import requests
import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus  
 #  quote_plus(), It safely converts special characters like

# API URL
url = "https://dummyjson.com/products"

# Fetch data
response = requests.get(url, verify=False, timeout=10)

data = response.json()

products = data["products"]

# Convert to DataFrame
df = pd.DataFrame(products)

# Convert nested JSON columns
import json

complex_columns = [
    "reviews",
    "meta",
    "dimensions",
    "images",
    "tags"
]

for column in complex_columns:
    df[column] = df[column].apply(json.dumps)


print(df.head())

# PostgreSQL connection
username = "postgres"
password = quote_plus("YOUR_PASSWORD")
host = "localhost"
port = "5432"
database = "retail_sales_db"

DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)

# Load data into PostgreSQL
df.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into PostgreSQL successfully!")