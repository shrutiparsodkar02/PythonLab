import time
#Approach 1
def get_even_odd_count1(l1):
	count_e=0
	count_o=0
	for i in l1:
		if i%2==0:
			count_e+=1
		else:
			count_o+=1
	return count_e,count_o
#print(get_even_odd_count([1,56,47,2,3]))
#Approach 2
def get_count(l):
	return True if l%2==0 else False 
def get_even_odd_count2(l1):
	count_e=0
	count_o=0
	for i in l1:
		if get_count(i):
			count_e+=1
		else:
			count_o+=1
	return count_e,count_o
#print(get_even_odd_count2([1,56,47,2,3]))
#Approach 3
def get_even_odd_count3(l1):
	count_e,count_o=0,0
	for i in l1:
		t=i%2
		#print(t)
		count_e=count_e+1-t
		count_o=count_o+t
	return count_e,count_o
#print(get_even_odd_count3([1,2,3,4]))
#Approach 4
def get_even_odd_count4(l1):
	count_e,count_o=0,0
	for i in l1:
		if i%2:
			count_o+=1
		else:
			count_e+=1
	return count_e,count_o
#print(get_even_odd_count4([1,2,3,4]))
#Approach5
def get_even_odd_count5(l1):
	count_e,count_o=0,0
	for i in l1:
		if i & 1:
			count_o+=1
		else:
			count_e+=1
	return count_e,count_o
#print(get_even_odd_count5([1,2,3,4]))
import time

def chek_performance(approaches, l):
    # List to store the average execution time for each approach
    time_final = []
    
    # Calculate the average execution time for each approach
    for approach in approaches:
        temp_time = []
        for _ in range(1000):
            start_time = time.time()
            approach(l)
            end_time = time.time()
            temp_time.append(end_time - start_time)
        avg_time = sum(temp_time) / 1000
        time_final.append(avg_time)
    # Comparing each approach to the first one
    print("Performance comparison:")
    for i in range(1, len(time_final)):
        if time_final[i] < time_final[0]:
            percentage = ((time_final[0] - time_final[i]) / time_final[0]) * 100
            print(f"Approach {i + 1} is {percentage:.2f}% faster than Approach 1")
        else:
            percentage = ((time_final[i] - time_final[0]) / time_final[0]) * 100
            print(f"Approach {i + 1} is {percentage:.2f}% slower than Approach 1")

# Example usage
chek_performance(
    [get_even_odd_count1, get_even_odd_count2, get_even_odd_count3, get_even_odd_count4, get_even_odd_count5],
    [1, 2, 3, 4]
)
'''def chek_performance(Approaches,l):
	time_final=[]
	for approach in Approaches:
		temp_time=[]
		for i in range(1000):
			start_time=time.time()
			approach(l)
			end_time=time.time()
			temp_time.append(end_time-start_time)
		time_final.append(sum(temp_time)/1000)
	per_list=[]
	print(time_final)
	for i in range(1,len(time_final)):
		#print("******************")
		first_app=time_final[0]*100
		
		per_cal=((time_final[0]-time_final[i])/time_final[0])*100
		#print(per_cal)
		per_list.append(int("%2.0f"%per_cal))
	#print(first_app)
	print(per_list)
	for i in per_list:
		if i<0:
			print(abs(i),"% slower then first approach")
		else:
			print(i,"% faster then first approach")
chek_performance([get_even_odd_count1,get_even_odd_count2,get_even_odd_count3,get_even_odd_count4,get_even_odd_count5],[1,2,3,4])'''
