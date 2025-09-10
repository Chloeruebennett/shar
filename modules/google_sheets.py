import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

class GoogleSheets:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        self.client = gspread.authorize(creds)

    def fetch_data(self, start_date: str, end_date: str):
        sheet = self.client.open("DataSheet").sheet1
        df = pd.DataFrame(sheet.get_all_records())

        df['date'] = pd.to_datetime(df['date'])
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        filtered = df[(df['date'] >= start_dt) & (df['date'] <= end_dt)]
        logging.info(f"Получено данных: {len(filtered)} строк")
        return filtered
