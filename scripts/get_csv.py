import csv
import os

import gspread
from credentials import get_service_account_credentials


def get_csv(sheet_id, csv_data_path):
    # This script uses google service accounts to authorize with the spreadsheet containing data,
    # (https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets)

    # Finds the json file with credentials for the service account, and authorizes the service account to gspread
    credentials = get_service_account_credentials()
    client = gspread.authorize(credentials)

    # Opens the spreadsheet containing data and gets all the values from the first index (page) of the spreadsheet
    spreadsheet = client.open_by_key(sheet_id)
    rows = spreadsheet.get_worksheet(0).get_all_values()

    csv_directory = os.path.dirname(csv_data_path)
    if not os.path.exists(csv_directory):
        os.makedirs(csv_directory)

    rows[0].append("FILNAMN")
    name_column_index = rows[0].index("NAMN")

    for row_index, row in enumerate(rows):
        # Skip the header row
        if (row_index == 0):
            continue

        name = row[name_column_index]
        file_name = name.replace(" ", "_")

        # Ensure file name does not include non-ASCII characters
        file_name = file_name.encode(encoding="ascii", errors="ignore")
        file_name = file_name.decode()

        file_name = f"{row_index + 1}_{file_name}.jpg"

        row.append(file_name)

    with open(csv_data_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
