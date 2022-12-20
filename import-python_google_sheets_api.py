from __future__ import print_function
import os.path
import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "phonic-agility-372114-c19e97dad9c4.json")
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1KVpdVDKx41-xRQeHcfi9E3LzM7kJ5N1F0arzpmjhAfY'
SAMPLE_RANGE_NAME = 'list_entered'
SAMPLE_RANGE_NAME2 = 'list_out'

service = build("sheets", "v4", credentials=credentials).spreadsheets().values()
result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()

for key, value in result.items():
        print(f'{key}: {value}')
values = result.get("values",[])

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)

DATA_TODAY = datetime.datetime.today().strftime("%d.%m.%Y")
print("печатаем сегодняшняя дата DATATODAY -",DATA_TODAY)
#SAMPLE_RANGE_NAME = 'A1:AA1000'

x = 1
def oo():
    for row in values:
                    for elem in row:
                        print("значение elem", elem)
                        global x
                        x = x + 1
                        range_2 = "List_out!A" + str(x)
                        print("печатаем range 2",range_2)
                        array = {'values': [[DATA_TODAY, elem]]}
                        response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                  range=range_2,
                                                  valueInputOption="USER_ENTERED",
                                                  body=array).execute()

oo()