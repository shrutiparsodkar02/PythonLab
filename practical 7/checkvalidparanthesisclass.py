'''def check_validity(text):
	alpa=["[","]","{","}","(",")",">","<"]
	text_list=list(text)
	#value=[91,93,123,125,40,41,60,62]
	for i in range(len(text)):
		if text[i] in alpa:
			while(i<len(text_list)):
				print(chr(ord(text[i])))
				print(chr(ord(text[i])+2))
				if chr(ord(text_list[i])) and chr(ord(text_list[i])+2) in text_list:
					text_list.pop(i)
					
					i+=1
				else:
					i+=1
			print("final list is-->",text_list)
		elif text=="":
			return "Valid"
		else:
			raise ValueError("Missmatch in alphabet")
print(check_validity("<{}]"))'''
def check_validity(text):
	pairs={"<":">","[":"]","{":"}","(":")"}
	stack=[]
	for symb in text:
		if symb in pairs:
			stack.append(symb)
		else:
			if(stack and symb==pairs[stack[-1]]):
				stack.pop()
			else:
				raise ValueError("Missmatch in alphabet")
		print(stack)
	if stack:
		return "invalid"
	else:
		return "Valid"
print(check_validity("<{}[]>"))
