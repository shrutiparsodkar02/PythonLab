def get_arr(l):
def get_arr(l):

    res = []
    for i in range(len(l)):
        if isinstance(l[i], (int, float)):
            res.append(l[i])
        elif isinstance(l[i], (list, tuple)):
            res.extend(get_arr(l[i])) 
        elif isinstance(l[i], dict):

            k = list(l[i].keys())
            v = list(l[i].values())
            res.extend(get_arr(k))
            res.extend(get_arr(v))
    res = list(set(res))  # Remove duplicates
    return res

def sort_list(n):
    # Sort the list using insertion sort
    for i in range(1, len(n)):
        curr = n[i]
        prev = i - 1
        while prev >= 0 and n[prev] > curr:
            n[prev + 1] = n[prev]
            prev -= 1
        n[prev + 1] = curr
    return n

def get_second_largest(l):
    # Get the array of numeric values
    res_arr = get_arr(l)
    if res_arr != []:
        sort_arr = sort_list(res_arr)
        if len(sort_arr) >= 2:
            return sort_arr[-2]  # Return second largest element
        else:
            return "Not enough numeric values to determine second largest"
    else:
        return "No numeric values found"

def get_second_smallest(l):
    # Get the array of numeric values
    res_arr = get_arr(l)
    if res_arr != []:
        sort_arr = sort_list(res_arr)
        if len(sort_arr) >= 2:
            return sort_arr[1]  # Return second smallest element
        else:
            return "Not enough numeric values to determine second smallest"
    else:
        return "No numeric values found"

# Test cases
l = ([2, 4, 8, [6, 7], (145, 89), 77], {10: "A", 507: 0, 45612: 123})
mixed_list = ["s", 3, 4]

print("Second largest in l:", get_second_largest(l))  # Expected: 145
print("Second smallest in l:", get_second_smallest(l))  # Expected: 4
print("Second largest in mixed_list:", get_second_largest(mixed_list))  # Expected: 3 (since only 3, 4 are numbers)
print("Second smallest in mixed_list:", get_second_smallest(mixed_list))  # Expected: 4
'''	#l=[2,4,8,[6,7],(145,89),77]
	res=[]
	for i in range(len(l)):
		if isinstance(l[i], (int,float)):
			res.append(l[i])
		elif isinstance(l[i],str):
			pass
		elif isinstance(l[i], (list, tuple)):
			res.extend(get_arr(l[i]))
		elif isinstance(l[i],dict):
			#print(l[i])
			k=list(l[i].keys())
			v=list(l[i].values())
			for i in range(len(k)):
				if isinstance(k,(int,float)):
					res.append(k)
				elif isinstance(v,(int,float)):
					res.append(v)
			res.extend(get_arr(k))
			res.extend(get_arr(v))
	res=list(set(res))
	print("--->",res)
	return res
l=([2,4,8,[6,7],(145,89),77],{10:"A",507:0,45612:123})
l2=[1,1,1,1,1]
get_arr(l2)
get_arr(["s","g"])
def sort_list(n):
	for i in range(1,len(n)):
		curr=n[i]
		prev=i-1
		#finding correct position to insert
		while(prev>=0 and n[prev]>curr):
			n[prev+1]=n[prev]
			prev-=1
		#insert into postion
		n[prev+1]=curr
	#print(n)
	return n
#sort_list([45,2,7,1,0,77,12])
def get_second_largest(l):
	res_arr=get_arr(l)
	if res_arr !=[] :
		sort_arr=sort_list(res_arr)
		if len(sort_arr)>=2:
			return sort_arr[-2] 
	else:
		return ValueError("No numeric value found")
def get_second_smallest():
	pass

#print(get_second_largest([2,4,8,[6,7],(145,89),77],{10:"A",507:0,45612:123}))'''


