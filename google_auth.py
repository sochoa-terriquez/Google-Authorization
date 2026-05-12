import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

CREDS = ServiceAccountCredentials.from_json_keyfile_name("keys.json", SCOPE)

client = gspread.authorize(CREDS)

sheet = client.open("BUS472")

worksheet = sheet.sheet1

if __name__ == "__main__":
    print("Accessible Spreadsheets..BUS472.")
    