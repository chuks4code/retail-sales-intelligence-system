import os

print("\nSTARTING RETAIL SALES PIPELINE\n")

# Run ETL pipeline
os.system("python load_to_postgres.py")

print("\nDATABASE UPDATE COMPLETE\n")

# Run monitoring system
os.system("python inventory_alerts.py")

print("\nMONITORING COMPLETE\n")

print("\nPIPELINE FINISHED SUCCESSFULLY\n")