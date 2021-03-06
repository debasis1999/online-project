def singleOne( num, n):
     
    res = num[0]
     
 
    for i in range(1,n):
        res = res ^ num[i]
     
    return res
 

num = [4, 1, 2, 1, 2 ]
print ("Element occurring once is", singleOne(num, len(num)))

num = [2,2,1]
print ("Element occurring once is", singleOne(num, len(num)))
