import crypt
import os
from subprocess import Popen, PIPE

#Resul Ucar

"""
To use, python3 dictionary.py
you will need a text file in the same directory as the script and 
each password should be on a seperate line
"""

#Asks for the username and stores it to a variable
var = input("Please enter username: ")

"""
enters sudo cat /etc/shadow | grep [username] '> shadow.txt into the terminal to open shadow file
searches the username in the file and saves the hash to a text file
"""
stdout = Popen('sudo cat /etc/shadow | grep '+var+ '> shadow.txt' , shell=True, stdout=PIPE).stdout
output = stdout.read()
#reads the text file for the hash
with open('shadow.txt', 'r') as file:
	shadow = file.read()

#splits the hash and salt
string = shadow.split(':')[1]
user = shadow.split(':')[0]
hashnum = string.split('$')[1]
salt = string.split('$')[2]
password = string.split('$')[3]

#creates a dictionary
d = {}
#boolean
flag = 0
#word puts the salt and hash type together and formats it for crypt function
word= '$'+hashnum+'$'+salt
#the path for the dictionary file
filepath = 'file.txt'
f = open(filepath)
lines = f.read().splitlines()
f.close()
#hashes every password in the dictionary file and stores the password and hash into a dictionary
for line in lines:
    crypter = crypt.crypt(line, word)
    d[line] = crypter
#compares the hash of the password to the hash of the users shadow file
for key, value in d.items():
	if value == string:
		flag = 2
#Results of the comparison
if flag == 2:
	print("Password for "+user+" is "+key)
else:
	print("Not Found")