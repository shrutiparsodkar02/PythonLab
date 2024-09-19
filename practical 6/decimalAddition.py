def deciamlAddition(num1,num2):
	#adding leading zeros
	max_len=max(len(num1),len(num2));
	num1=num1.zfill(max_len)
	num2=num2.zfill(max_len)
	#print(num1,num2)
	num1_lsb=[]
	num2_lsb=[]
	int_l1=[]
	int_l2=[]
	#converting string to integer
	for j in range(1,len(num1)+1):
		num1_lsb=num1[-(j)]
		num2_lsb=num2[-(j)]
		print("num1-->",num1_lsb,"----","num2-->",num2_lsb)
		int_l1+=[ord(num1_lsb)-48]
		int_l2+=[ord(num2_lsb)-48]
	#print(int_l1,int_l2)
	#performin decimal addition
	result=[]
	carry=0
	for i in range(len(int_l1)):
		temp_result=int_l1[i]+int_l2[i]+carry
		carry=temp_result//10
		result.append(temp_result%10)
	if carry:
		result.append(carry)
	result.reverse()
	final_res="".join(map(str,result))
	print(final_res)
deciamlAddition("1452","12")
