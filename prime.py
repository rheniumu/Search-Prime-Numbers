# Generate Prime Number List

import time
import math

def isPrime(p,lis):
	p = abs(p)
	if pow(2,p - 1,p) == 1:
		i = 2
		flag = True
		for i in lis:
			if i >= math.sqrt(p):
				break
			if p % i == 0:
				flag = False
				break
		
		return flag
	else:
		return False

lis = [2,3]
a = input("整数を入力 : ")
if a.isdigit() == True:
	a = int(a)
else:
	print("整数を入力してください")
	quit()

startTime = time.time()

for i in range(a - 3):
	if isPrime(i + 4,lis) == True:
		#print(i + 4)
		lis.append(i + 4)

endTime = time.time()

print(lis)
print(endTime - startTime)


