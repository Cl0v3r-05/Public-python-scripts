# YOU WILL NEED YOUR OWN GOOGLE SHEETS API KEY
# LOOK UP A TUTORIAL ON HOW TO OBTAIN ONE IF YOU 
# DON'T KNOW HOW.
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import secrets
import string
import time
import datetime
now = datetime.datetime.now() # stores the date and time the program started

alphabet = string.digits # sets the module to generate numbers

pwd_length = 4 # sets number length

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
] # sets urls to access for service credentials

credentials = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes) # access the json key you downloaded
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("numberexperiment") # open sheet, change "numberexperiment" to whatever your file is named.
sheet = sheet.sheet1 # replace sheet_name with the name that corresponds to yours

sheet.update('G2', [[str(now)]]) # prints date and time program started to cell G2
time.sleep(1) # waits to prevent API errors, see line 50 for more info

while True:
    pwd = ''  # Sets "pwd" 1-4 to a blank variable to allow for generated value to be stored and clears variable every loop
    pwd2 = ''
    pwd3 = ''
    pwd4 = ''
    for i in range(pwd_length):  # Tells program to generate the numbers 
        pwd += ''.join(secrets.choice(alphabet)) 
    for i in range(pwd_length):
        pwd2 += ''.join(secrets.choice(alphabet))
    for i in range(pwd_length):
        pwd3 += ''.join(secrets.choice(alphabet))
    for i in range(pwd_length):
        pwd4 += ''.join(secrets.choice(alphabet))

    


    print('done generating') # prints this to confirm numbers have been generated
    sheet.update('C1:C4', [[pwd],[pwd2], [pwd3], [pwd4]]) # sets cells C1 to cell C4 to contain the 4 generated numbers
    total = int(pwd) + int(pwd2) + int(pwd3) + int(pwd4) # Adds all the generated numbers 
    sheet.update('A1', [[total]]) # Prints the sum of the numbers to cell A1
    time.sleep(2) # waits 2 seconds to prevent API errors. You have 60 "write" actions aloted per minute(one per second), since this writes 2 times in a second it waits
                  # 2 seconds to prevent going over the 60 writes per minute.
    if total == int(30000): # compairs the sum to 30000
        sheet.update('E2', [[total]]) # If the sum is 30000 it prints the total in cell E2
        sheet.update('I2', [[now]]) # If match is found the end time is printed in cell I2
        break # Breaks loop if match is found
print('match found') # Prints match found to notify that the match is found
