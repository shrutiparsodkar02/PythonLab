 def change_case(text,style):
#for capital case--->
	if style=="c"or style=="C":
		def convert_capital_case(text):
			len_str=len(text)
			String=""
			for i in range(len_str):
				if(ord(text[i])>=97 and ord(text[i])<=122 ):
					res=ord(text[i])-32
					res2=chr(res)
					String+=res2
				else:
					String+=text[i]
			print(String)
			return String		
		return convert_capital_case(text)
#for lower case---->
	elif style=="S"or style=="s":
		def convert_lower_case(text):
			len_str=len(text)
			String=""
			for i in range(len_str):
				if(ord(text[i])>=65 and ord(text[i])<=90):
					res=ord(text[i])+32
					res2=chr(res)
					String+=res2
				else:
					String+=text[i]
			print(String)
			return String	
		return convert_lower_case(text)
#for reverse case---->
	elif style=="r" or style=="R":
		def convert_reverse_case(text):
			len_str=len(text)
			String=""
			for i in range(len_str):
				if(ord(text[i])>=65 and ord(text[i])<=90):
					res=ord(text[i])+32
					res2=chr(res)
					String+=res2
				elif(ord(text[i])>=97 and ord(text[i])<=122 ):
					res=ord(text[i])-32
					res2=chr(res)
					String+=res2
				else:
					String+=text[i]
			print(String)
			return String
		return convert_reverse_case(text)
#for zigzag case--->
	elif style=="Z" or style=="z":
		def convert_zigzag_case(text):
			len_str=len(text)
			String=""
			
			for i in range(len_str):
				char = text[i]
				if ord(text[i])>=97 and ord(text[i])<=122:  # If the character is lowercase
					if i % 2 == 0:
               				 # Convert to uppercase by subtracting 32 from ASCII value
						String += chr(ord(char) - 32)
					else:
						String += char  # Keep it lowercase
				elif ord(text[i])>=65 and ord(text[i])<=90:  # If the character is uppercase
					if i % 2 == 0:
						String += char  # Keep it uppercase
					else:
					
						String += chr(ord(char) + 32)
				else:
					String += char  # For non-alphabetic characters, add as it is
			return String
		return convert_zigzag_case(text)
res=change_case("1234shruti","z")
print(res)

