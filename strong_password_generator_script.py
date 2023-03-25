#Peogram to create strong password
#Password at least 6 characters (upper/lower case , numbers & punctuations) 
#password 60% letters , 40% digits and punctuations

import string #importing string module that including all characters
import random #importing random module 
s1 = list(string.ascii_lowercase) #import lower case letters 
s2 = list(string.ascii_uppercase) #import upper case letters 
s3 = list(string.digits) #import numbers 
s4 = list(string.punctuation) #import punctuations 

chracters_number = input('''password generator script .. 
Enter the numbers of password characters : ''')
while True : 
    try:
        chracters_number = int(chracters_number)
        if chracters_number < 6 : 
            print ("to create a strong password tou need at least 6 characters")
            chracters_number = input("plzzz enter the number again :")
        else : 
            break
    except : 
        print ("plz enter numbers only ")
        chracters_number = input("Enter the number again : ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4) 

part1 = round(chracters_number * (30/100)) 
part2 = round(chracters_number * (20/100))

password = []

for i in range (part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range (part2):
    password.append(s4[i])
    password.append(s3[i])

random.shuffle(password)

password  = "".join(password) 

print (password)
