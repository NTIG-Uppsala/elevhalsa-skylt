import csv
import subprocess
import time
import sys
import gspread
import os
from credentials import get_service_account_credentials


# This script uses google service accounts to authorize with the spreadsheet containing data,
# (https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets)
# cli arguments are used in the script to specify path and sheet id

# Finds the json file with credentials for the service account, and authorizes the service account to gspread
credentials = get_service_account_credentials()
client = gspread.authorize(credentials)

# Opens the spreadsheet containing data and gets all the values from the first index (page) of the spreadsheet
sh = client.open_by_key(sys.argv[1])
rows = sh.get_worksheet(0).get_all_values()

csv_path = sys.argv[2]
csv_directory = os.path.dirname(csv_path)

if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

rows[0].append("FILNAMN")
name_column_index = rows[0].index("NAMN")

for row_index in range(1, len(rows)):
    row = rows[row_index]
    name = row[name_column_index].replace(" ", "_")
    row_number = row_index + 1
    file_name = f"{row_number}_{name}.jpg"
    row.append(file_name)

with open(csv_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
        
