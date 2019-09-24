 
def PairsofSum(arr, n, k): 
    count = 0
    list = []
    # Pick all elements one by one 
    for i in range(0, n): 
          
        # See if there is a pair of this picked element 
        for j in range(i+1, n) : 
              
            if arr[i] + arr[j] == k or arr[j] + arr[i] == k: 
                count += 1
                list.append((arr[i],arr[j])) 
    return count ,list
  

arr = [1, 9, 4, 6, 7,8,0] 
  
n = len(arr) 
k = 10
count, list = PairsofSum(arr, n, k)
print ("Count of pairs with given diff is ", count, "\tThe list of pairs is: ", list) 