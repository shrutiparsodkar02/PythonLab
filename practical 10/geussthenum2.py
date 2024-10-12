#geuss number and win prize
import random
def inti(s,e):
	print("----WELCOME-----")
	sn=random.randint(s,e)
	print(sn)
	return sn
def start_game(sn,s,e):
	status=False
	prizes={1:5,2:3,3:2,4:1,5:0}
	amount=int(input("enter the amount you want to bet  -->"))
	i=0
	count=0
	while i<5:
		geuss=int(input(f"attempt {i+1} enter your geuss between {s} to {e}--->"))
		count+=1
		if geuss==sn:
			print(f"congrats you won in {i+1} attempts")
			break
		i+=1
	else:
		print(f"sorry you have used all your attempts")
	prize_money=prizes.get(count,0)*amount
	if prize_money>0:
		print(f"congrats you won {prize_money} RS")
		status=True
	else:
		print("You got 0  RS")
	return status

def stop_game(status):
	if status:
		print("****---------congrats---------****")
	else:
		print("sorry no correct geuss,--you loose---,BETTER LUCK NEXT TIME ")
s=1
e=5
#inti(s,e)
sn=inti(s,e)
status=start_game(sn,s,e)
stop_game(status)

