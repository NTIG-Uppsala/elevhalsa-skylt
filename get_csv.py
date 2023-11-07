import csv
import sys
import gspread
import os
from credentials import get_service_account_credentials
from dotenv import load_dotenv

# Loads content of enviroment variable file, default path is `./.env`
load_dotenv()

DEFAULT_CSV_DATA_PATH = "./site/data/stored_data.csv"

#If code runs without any arguments, run with default options
if len(sys.argv) == 1:
     sheet_id = os.getenv("sheet_id") # Fetches sheet id from env 
     csv_path = DEFAULT_CSV_DATA_PATH
else:
    try:
        sheet_id = sys.argv[1]
        csv_path = sys.argv[2]
    except:
        print("Error: usage py get_csv.py <sheet_id> <data_path>")
        sys.exit(-1)

# This script uses google service accounts to authorize with the spreadsheet containing data,
# (https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets)
credentials = get_service_account_credentials()
client = gspread.authorize(credentials)

# Opens the spreadsheet containing data and gets all the values from the first index (page) of the spreadsheet
try:
    sh = client.open_by_key(sheet_id)
    rows = sh.get_worksheet(0).get_all_values()
# If no or incorrect path is given as an argument
except: 
    print("Error: get_csv.py could not get path")
    sys.exit(-1)


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

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        
