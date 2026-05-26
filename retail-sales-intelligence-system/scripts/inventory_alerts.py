from dotenv import load_dotenv 
import os 
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()



# PostgreSQL connection
username = "postgres"
password = quote_plus(os.getenv("DB_PASSWORD"))
host = "localhost"
port = "5432"
database = "retail_sales_db"

DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)

# “Save log messages into inventory_alerts.log”
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(BASE_DIR, "logs", "inventory_alerts.log")
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = EMAIL_ADDRESS

# send email alert function
def send_email_alert(subject, body):

    msg = MIMEMultipart()

    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.send_message(msg)


# Load products table
query = "SELECT title, stock, category FROM products"

df = pd.read_sql(query, engine)

# Low inventory threshold
LOW_STOCK_THRESHOLD = 20

# Find low stock products
low_stock = df[df["stock"] < LOW_STOCK_THRESHOLD]
# “ df["stock"] < 20 Which stock values are less than 20?” 
# “Return only rows where condition is True.” that is where products with low inventory.

if low_stock.empty:
      message = "No low inventory issues found."
      print(message)
      logging.info(message)
else:

    print("\nLOW STOCK ALERTS\n")

    all_alerts = []

    for index, row in low_stock.iterrows():

        product_name = row["title"]
        category_name = row["category"]
        stock_left = row["stock"]

        alert_message = (
            f"ALERT: {product_name} "
            f"in category '{category_name}' "
            f"has only {stock_left} units left."
        )

        print(alert_message)

        logging.warning(alert_message)

        all_alerts.append(alert_message)

    email_body = "\n\n".join(all_alerts)

    send_email_alert(
        "LOW INVENTORY ALERT SUMMARY",
        email_body
    )