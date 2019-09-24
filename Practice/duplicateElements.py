a = list(input("Please Enter the List: "))

d = dict((i, a.count(i)) for i in a)

print("Values and Occurances are : ",d)
