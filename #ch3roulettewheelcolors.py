#ch3roulettewheelcolors.py

def userinput():
	prompt=int(input('Enter a pocket number between 0 to 36: '))

	return prompt


def colorwheel(pocket):

	if pocket==0:
		print('The pocket is green')
	elif pocket>=1 and pocket<=10:
		if pocket % 2 == 0:
			print('The pocket is red')
		else:
			print('The pocket is black')
	elif pocket>=11 and pocket<=18:
		if pocket % 2 == 0:
			print('The pocket is black')
		else:
			print('The pocket is red')
	elif pocket>=19 and pocket<=28:
		if pocket % 2 == 0:
			print('The pocket is red')
		else:
			print('The pocket is black')
	elif pocket>=29 and pocket<=36:
		if pocket % 2 == 0:
			print('The pocket is black')
		else:
			print('The pocket is red')
	else:
		print("Error: Pocket Selected is Out-of-Range. Please try again.")


def main():

	print("Lets play Roulette Wheel!")

	colorwheel(userinput())



main()

