import os

import get_csv
import get_images
from dotenv import load_dotenv

CSV_DATA_PATH = "./site/_data/stored_data.csv"

# Loads content of environment variable file, default path is `./.env`
load_dotenv()
sheet_id = os.getenv("sheet_id")

get_csv.get_csv(sheet_id, CSV_DATA_PATH)
get_images.get_images(sheet_id, CSV_DATA_PATH)
