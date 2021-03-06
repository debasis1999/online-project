def Intersection(num1, num2, m, n): 
     i, j = 0, 0
     while i < m and j < n: 
        if num1[i] < num2[j]: 
		i += 1
	elif num2[j] < num1[i]: 
		j+= 1
	else: 
		print(num2[j]) 
		j += 1
		i += 1


num1 = [4, 9, 5] 
num2 = [9, 4, 9, 8, 4] 
m = len(num1) 
n = len(num2) 
print(Intersection(num1, num2, m, n) )
