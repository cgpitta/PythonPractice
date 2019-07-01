#ch7primenumbergneration.py


def userval():

	prompt=int(input("Enter an integer greater than 1: "))

	while prompt <=1:
		print("Hey Asshole! I said the integer must be greater than 1. Do it again!")

		prompt=int(input("Enter an integer greater than 1: "))


	return prompt

def is_prime(num):

	if num < 2:
		return False

	else:

		for n in range(2,num):
			if num%n==0:
				return False

	return True



def main():

	number=userval()

	
	numberlist=[]


	for n in range(2, number):

		numberlist.append(n)


	for n in range(len(numberlist)):

		if is_prime(numberlist[n]) == True:

			print(numberlist[n])


main()





