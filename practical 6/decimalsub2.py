def decimal_sub2(num1,num2):
	n1=list(num1)
	n2=list(num2)
	len_num1=len(n1)
	len_num2=len(n2)
	sub_len=abs(len_num1-len_num2)
	print(sub_len)
	num1_lsb=0
	num2_lsb=0
	int_l1=[]
	int_l2=[]
	if(len_num1>len_num2):
		n2=[]
		i=0
		while(i<sub_len):
			n2.append(str(0))
			i+=1
		n2+=list(num2)
	elif(len_num1<len_num2):
		n1=[]
		i=0
		while(i<sub_len):
			n1.append(str(0))
			i+=1
		n1+=list(num1)
	#print(n1,n2)
	for j in range(1,len(n1)+1):
		num1_lsb=n1[-(j)]
		num2_lsb=n2[-(j)]
		#print("num1-->",num1_lsb,"----","num2-->",num2_lsb)
		int_l1+=[ord(num1_lsb)-48]
		int_l2+=[ord(num2_lsb)-48]
	int_n1_final=int_l1[::-1]
	int_n2_final=int_l2[::-1]
	print(int_n1_final,int_n2_final)
	num1_lsb_final=0
	num2_lsb_final=0
	final_answer=[]
	carry=0
	sign=-1
	for j in range(1,len(n1)+1):
		num1_lsb_final=int_n1_final[-(j)]
		num2_lsb_final=int_n2_final[-(j)]
		print("num1-->",num1_lsb_final,"num2--->",num2_lsb_final)
		if(num1_lsb_final==num2_lsb_final):
			final_answer+=[0]
		elif(num1_lsb_final>num2_lsb_final):
			final_answer+=[num1_lsb_final-num2_lsb_final]
		elif(num1_lsb_final<num2_lsb_final):
			final_answer+=sign*[num2_lsb_final-num1_lsb_final]
	print("final answer--->",final_answer)
num1="2456"
num2="518"
decimal_sub2(num1,num2)
