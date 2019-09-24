# Python Program to Calculate Electricity Bill
# units <= 100 -- 2rupees/unit
#100<units < 250  -- 5rupes/unit
# 250 < units < 400 -- 8/unit
# >400 units -- 10/unit 
 
units = int(input(" Please enter Number of Units you Consumed : "))

if(units < 100):
    amount = units * 2
    surcharge = 25
elif(units <= 250):
    amount = 200 + ((units - 50) * 5)
    surcharge = 35
elif(units <= 400):
    amount = 200 + 750 + ((units - 100) * 8)
    surcharge = 45
else:
    amount = 200 + 750 + 1200 + ((units - 400) * 10)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = ",  total)