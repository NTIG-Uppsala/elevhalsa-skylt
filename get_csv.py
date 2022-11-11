import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_login.json', scope)
client = gspread.authorize(credentials)
sh = client.open_by_key("1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs")

rows = sh.get_worksheet(0).get_all_values()
print(rows)
print("åäö")
with open("stored_data", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        for val in row:
            pass
            #print(val)
        writer.writerow(row)