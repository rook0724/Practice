import random
list=[]

while(len(list)<3):
    
    r=random.randint(1,10)
    if r not in list:list.append(r)

print("List",list)

  
