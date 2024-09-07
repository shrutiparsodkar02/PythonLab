'''def binarySubtraction(num1,num2):
	max_len=max(len(num1),len(num2))
	num1=num1.zfill(max_len)
	num2=num2.zfill(max_len)
	print(num1,num2)
	n1=list(num1);
	n2=list(num2);
	num1_lsb=0
	num2_lsb=0
	int_l1=[]
	int_l2=[]
	borrow=0
	diff=0
	res=0
	for j in range(1,len(n1)+1):
		num1_lsb=n1[-(j)]
		num2_lsb=n2[-(j)]
		#print("num1-->",type(num1_lsb),"----","num2-->",num2_lsb)
		int_l1+=[ord(num1_lsb)-48]
		int_l2+=[ord(num2_lsb)-48]
	int_n1_final=int_l1[::-1]
	int_n2_final=int_l2[::-1]
	print(int_n1_final,int_n2_final)
	for i in range(len(int_n1_final)-1,-1,-1):
		bit1=int_n1_final[i]
		bit2=int_n2_final[i]
		print("bit1-->",bit1,"bit2--->",bit2)
		diff=bit1-bit2-borrow
		if diff<0:
			diff+=2
			borrow+=1
		else:
			borrow=0
	res+=diff
	print(diff)
	#for i in range(len())
binarySubtraction("1101","1010")'''
def binarySubtraction(num1, num2):
    # Ensure both binary strings have the same length
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    print(num1, num2)
    
    # Convert to integer lists (0 or 1)
    int_l1 = [1 if bit == '1' else 0 for bit in num1]
    int_l2 = [1 if bit == '1' else 0 for bit in num2]
    
    print(int_l1, int_l2)
    
    result = []
    borrow = 0
    
    # Perform binary subtraction
    for i in range(len(int_l1) - 1, -1, -1):
        bit1 = int_l1[i]
        bit2 = int_l2[i]
        print("bit1-->", bit1, "bit2--->", bit2)
        
        diff = bit1 - bit2 - borrow
        
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(diff))
        print(diff)
    
    # Reverse the result and remove leading zeros
    result = ''.join(result[::-1]).lstrip('0')
    
    # Return '0' if result is empty
    return result if result else '0'

# Example usage
print(binarySubtraction("1101", "1010"))  # Output should be '11'

