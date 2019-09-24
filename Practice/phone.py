import re
password=input("Input password := ")
pattern = re.compile('^[6-9]$|^[0-9]\d{9}$')
a=re.search(pattern,password)
if a==None:
    print("This password is not valid")
else:
    print("This password is valid")
