import os

import get_csv

import get_images
from dotenv import load_dotenv

CSV_DATA_PATH = "./site/_data/stored_data.csv"
EVENT_CSV_DATA_PATH = "./site/assets/stored_event_data.csv"

load_dotenv()
sheet_id = os.getenv("sheet_id")

get_csv.get_csv(sheet_id, CSV_DATA_PATH, EVENT_CSV_DATA_PATH)
get_images.get_images(sheet_id, CSV_DATA_PATH)
