'''def get_valid_invalid(text):
	pairs={"<":">","[":"]","{":"}","(":")"}
	stack=[]
	valid_count=0
	invalid_count=0
	for symb in text:
		print("--->",symb)
		if symb in pairs:
			stack.append(symb)
		else:
			if(stack and symb==pairs[stack[-1]]):
				stack.pop()
			else:
				raise ValueError("Missmatch in alphabet")
		print(stack)
	if stack:
		invalid_count+=1
	else:
		valid_count+=1
	return valid_count,invalid_count
def get_count(text):
	valid_count=0
	invalid_count=0
	for i in range(len(text)):
		if type(text[i])==list:
			res=get_valid_invalid(text)
			valid_count+=res[0]
			invalid_count+=res[1]
		elif type(text[i])==int:
			pass
		elif type(text[i])==set:
			res=text=list(text)
			valid_count+=res[0]
			invalid_count+=res[1]
			get_valid_invalid(text)
		elif type(text[i])==tuple:
			res=get_valid_invalid(text)
			valid_count+=res[0]
			invalid_count+=res[1]
	return valid_count,invalid_count
#print(get_valid_invalid([[],"(})",[45,("()"),{}]]))
print(get_count([[],"(})",[45,("()"),{}]]))'''
def get_valid_invalid(text):
    pairs = {"<": ">", "[": "]", "{": "}", "(": ")"}
    stack = []
    valid_count = 0
    invalid_count = 0
    for symb in text:
        if symb in pairs:
            stack.append(symb)
        elif stack and symb == pairs.get(stack[-1]):
            stack.pop()
    if stack:
        invalid_count += 1
    else:
        valid_count += 1
    return valid_count, invalid_count

def get_count(text):
    valid_count = 0
    invalid_count = 0
    for item in text:
        if isinstance(item, str):
            res = get_valid_invalid(item)
            valid_count += res[0]
            invalid_count += res[1]
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            # Convert sets and tuples
            res = get_count([str(sub_item) for sub_item in item])
            valid_count += res[0]
            invalid_count += res[1]
    return valid_count, invalid_count

# Test case
print(get_count([[[]],(),{"<"}]))

