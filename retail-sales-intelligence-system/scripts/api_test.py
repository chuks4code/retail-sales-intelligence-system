
import os
import requests
import pandas as pd

url = "https://dummyjson.com/products"

response = requests.get(url, verify=False, timeout=10)

data = response.json()

products = data["products"]

df = pd.DataFrame(products)

print(df.head())

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

output_path = os.path.join(BASE_DIR, "data", "products.csv")

df.to_csv(output_path, index=False)

print("CSV file created successfully!")