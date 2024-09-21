import time
def int_fun():
	for num in range(10,20,2):
		num=num*1.0
		y=int(num)
		#print(num)
		#print(y)
def int_opr():
	for num in range(10,20,2):
		num=num*1.0
		y=num//1
		#print(num)
		#print(y)
def check_performance(approaches):
	time_spent=[]
	for approach in approaches:
		temp_time=[]
		for _ in range(10000):
			start_time=time.time()
			approach()
			end_time=time.time()
			temp_time.append(end_time-start_time)
			#print(temp_time)
		time_spent.append(sum(temp_time)/10000)
	return list(zip(approaches,time_spent))
print(check_performance([int_opr,int_fun]))
