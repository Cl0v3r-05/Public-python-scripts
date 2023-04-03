from oauth2client.service_account import ServiceAccountCredentials
import gspread
import secrets
import string
import time
import datetime
now = datetime.datetime.now()

alphabet = string.digits

pwd_length = 4
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("numberexperiment") #open sheet
sheet = sheet.sheet1 #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

sheet.update('G2', [[str(now)]])
time.sleep(1)

while True:
    pwd = ''  # Sets "pwd" 1-3 to a blank variable to allow for generated value to be stored and clears variable every loop
    pwd2 = ''
    pwd3 = ''
    pwd4 = ''
    for i in range(pwd_length):  # Tells program to only generate 12 digits
        pwd += ''.join(secrets.choice(alphabet)) 
    for i in range(pwd_length):
        pwd2 += ''.join(secrets.choice(alphabet))
    for i in range(pwd_length):
        pwd3 += ''.join(secrets.choice(alphabet))
    for i in range(pwd_length):
        pwd4 += ''.join(secrets.choice(alphabet))

    


    print('done')
    sheet.update('C1:C4', [[pwd],[pwd2], [pwd3], [pwd4]])
    total = int(pwd) + int(pwd2) + int(pwd3) + int(pwd4)
    sheet.update('A1', [[total]])
    time.sleep(2)
    if total == 40000:
        sheet.update('E2', [[total]])
        sheet.update('I2', [[now]])
        break
print('match found')
