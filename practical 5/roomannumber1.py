def room(text,textbase):
	if(text.isdigit() and textbase.isdigit()):
		num=[]
		for i in range(len(text)-1,-1,-1):
			elem=text[i]
			num.append(elem)
		#print(num)
		val_j=[]
		for j in range(len(text)):
			val_j.append(j)
		#print(val_j)
		sum=0
		for i in range(len(num)):
			sum+=int(num[i])*(pow(int(textbase),val_j[i]))
		#print("after conversion value is-->",sum)
		#return sum
	elif(not(textbase.isdigit())):
		raise ValueError ("Invalid textbase")
	else:
		raise ValueError ("Invalid text entered")
	#for converting in rooman num
	val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
	symbol=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
	rom_num=""
	for i in range(len(val)):
		while(sum>=val[i]):
			rom_num+=symbol[i]
			sum-=val[i]
	return rom_num
res=room("23","16")
print(res)
