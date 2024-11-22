#check for leap year
def check_leap_year(year):
	return (year%4==0 and year%100!=0) or (year%400==0)
#check number of days in month
def get_no_days_month(month,year):
	days_of_months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	if month == 2 and check_leap_year(year):
		return 29
	else:
		return days_of_months[month]
def get_first_day_of_month(year):
	reference_year=1900
	first_day=1
	total_shift=0
	for i in range(reference_year,year):
		total_shift+=2 if check_leap_year(i) else 1
	return (total_shift+reference_year)%7
def genrate_calender(year):
	days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	months = [
	"January", "February", "March", "April", "May", "June",
	"July", "August", "September", "October", "November", "December"]
	for month in range(1,13):
		print("_"*10,months[month-1],"_"*10,year)
		print("\n")
		for j in days_of_week:
			print("|",j,"|",end="\t")
		print()
		first_day=get_first_day_of_month(year)
		num_days=get_no_days_month(month,year)
		print("\t" * first_day, end="")
		for day in range(1,num_days+1):
			print("|",day," |" if len(str(day))==1 else "|",end="\t")
			if(day+first_day)%7==0:
				print()
		print("\n")
	print("\n")
year=eval(input("enter year for which you want to genrate calender---->"))
#print(check_leap_year(year))
#print(get_no_days_month(2,year))
genrate_calender(year)
