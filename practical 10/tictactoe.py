import random 
'''def display_gs(size):
	size=size+1
	#val={1:" ",2:" ",3:" "}
	val=dict(zip(range(1,size),(" ")*size))
	#print(val)
	gs_1=dict(zip(range(1,size),[val]*size))
	#print(gs_1)
	return gs_1
	
	#print(len(gs_1))
#display_gs(7)
def print_grid():
	
def play_game(gs_s,size):
	player1=input("enter Player 1------>")
	player2=input("enter Player 2------>")
	if player1:
		val="@"
	else:
		val="$"
	for i in range(size**2):
		player=random.randint(1,2)
		if player==1:
			print(f"{player1} TURNS")
		else:
			print(f"{player2} TURNS")
		coordinate=input("enter your location where you want to insert your valur in (x,y) formate")
	if gs_s[coordinate[0]][coordinate[1]]==" ":
		gs_s[coordinate[0]][coordinate[1]]=val
	else:
		print("enter other location its already occupied")
size=int(input("enter the size which you weant to play-->"))
gs_s=display_gs(size)
play_game(gs_s,size)'''
def display_gs(size):
	grid={(x,y):" " for x in range(1,size+1) for y in range(1,size+1)}
	return grid
#print(display_gs(3))
def print_grid(grid,size):
	for i in range(1,size+1):
		row="|".join(grid[i,y] for y in range(1,size+1))
		print(row)
		if i !=size:
			print("-"*(2*size))
size=3
#grid=display_gs(size)
def winingpattern(size,symbol,grid):
	#vertical check
	for i in range(1,size+1):
		if all(grid[(i,j)]==symbol for j in range(1,size+1)):
			return True
	#horizontal check
	for j in range(1,size+1):
		if all(grid[(i,j)]==symbol for i in range(1,size+1)):
			return True
	#diagonal check
	if all(grid[(i,i)]==symbol for i in range(1,size+1)):
		return True
	#anti daigonal check
	if all(grid[(i,size+1-i)]==symbol for i in range(1,size+1)):
		return True
	return False
def play_game(grid,size):
	count=0
	player1=input("enter name of player 1")
	player2=input("enter name of player 2")
	sym={player1:"@",player2:"$"}
	geuss_chance=random.randint(1,2)
	for i in range(size**2):
		print_grid(grid,size)
		current_player=player1 if geuss_chance==1 else player2
		print(f"{current_player} turns--->{sym[current_player]}")
		while True:
			try:
				x,y=map(int,input("enter co-ordinates where you want to place symbol-->in (x,y) formate").split(","))
				if 1<=x<=size and 1<=y<=size:
					if grid[(x,y)]==" ":
						grid[(x,y)]=sym[current_player]
						count+=1
						break
					else:
						print("please enter other coordinate the spot is already occupied")
				else:
					print("please enter the co-ordinates between 1 to {size} range")
			except ValueError:
				print("INVALID INPUT FORMATE please enter in (x,y) formate")
		if winingpattern(size,sym[current_player],grid):
			print_grid(grid,size)
			print(f"congrats {current_player} wins")
			return
		geuss_chance=2 if geuss_chance==1 else 1
	print_grid(grid,size)
	print("	ITS TIE ")
print("TIC TAC TOE")
size=int(input("enter the size in which you want to play"))
grid=display_gs(size)
play_game(grid,size)
