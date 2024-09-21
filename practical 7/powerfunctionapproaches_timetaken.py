import time
def pow_fun():
	for i in range(10,100,2):
		y=pow(i,2)
def pow_opr():
	for i in range(10,100,2):
		y=i**2
def check_performance(approaches):
	time_taken=[]
	for approach in approaches:
		temp_time=[]
		for _ in range(1000):
			start_time=time.time()
			approach()
			end_time=time.time()
			temp_time.append(end_time-start_time)
			#print(zip(approach,temp_time))
		time_taken.append(sum(temp_time)/1000)
	return list(zip(approaches,time_taken))
		#print("***",time_taken)
print(check_performance([pow_fun,pow_opr]))
