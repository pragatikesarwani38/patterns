row=4
#outer
for i in range(65,70):
	row=row-1
	for j in range(row,1,-1):
		print(" ",end=" ")
	for k in range(65,i+1):
		print(chr(k),end=" ")
	for n in range(65,i):
		print(chr(n),end=" ")
	print()