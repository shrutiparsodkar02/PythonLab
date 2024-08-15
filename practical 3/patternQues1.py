def print_pattern(n):
	n+=1
	k=n-1
	
	#upper half
	for i in range(n):
		for j in range(n):
			if((i+j)/k==1):
				print("*",end="  ")
			elif(i==j==(n-1)):
				print(j,end="  ")
			else:
				print(" ",end="  ")
		for j in range(1,n):
			if(i==j):
				print("*",end="  ")
			elif(i==j==(n-1)):
				print(j,end="  ")
			else:
				print(" ",end="  ")
		print()
	#lower half triangle
	for i in range(1,n-1):
		for j in range(n):
			
			if(i==k and j==k):
				print(" ",end="  ")
			elif(i==j):
				print("*",end="  ")
			else:
				print(" ",end="  ")
		#print()
		for j in range(1,n):
			if((i+j)/k==1):
				print("*",end="  ")
			
			else:             
				print(" ",end="  ")
		print()
	'''d=1;
		m=2*(n-1)+1
		while(d<n):
		#print("",end="")
		for i in range(m):
			print("*",end=" ")
		d+=1
		print()'''
	m=2*(n-1)+1
	for i in range(1,n):
		for j in range(m):
			print("*",end="  ")
		print()
	
print_pattern(20)
