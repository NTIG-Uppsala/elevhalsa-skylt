import csv
import subprocess
import time
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# This script uses google service accounts to authorize with the spreadsheet containing data,
# (https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets)

# URLs the service account uses to authorize to google spreadsheets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Finds the json file with credentials for the service account, and authorizes the service account to gspread
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "client_login.json", scope
)
client = gspread.authorize(credentials)


# Opens the spreadsheet containing data and gets all the values from the first index (page) of the spreadsheet
sh = client.open_by_key(sys.argv[1])

rows = sh.get_worksheet(0).get_all_values()

# Opens the current csv file with data, then reads and saves every row in a list
current_sheet = []


def read_csv_file_to_sheet(path, sheet):
    with open(path, "r", encoding="utf-8") as r:
        sheet = []
        csvreader = csv.reader(r)
        for row in csvreader:
            sheet.append(row)


csv_path = "site/_data/stored_data.csv"

if len(sys.argv) > 0:
    csv_path = "tests/stored_data.csv"
try:
    read_csv_file_to_sheet(csv_path, current_sheet)
except:
    open(csv_path, "x", encoding="utf-8")
    read_csv_file_to_sheet(csv_path, current_sheet)

# Compares currently saved csv data with the data on the spreadsheet, and updates it if changes has been made
if current_sheet != rows:
    # removes empty lists from currentSheet
    current_sheet = [item for item in current_sheet if item != []]
    print("Data changed, updating...")
    with open(csv_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    print("Data has been updated, refreshing page!")

    # Refreshes the page after two seconds if change has been found (delay is for syncing reasons)
    time.sleep(2)
    try:
        subprocess.run(["xdotool", "key", "F5"])
    except:
        print("Error: Ignore this error if you are not in Raspberry pi")
