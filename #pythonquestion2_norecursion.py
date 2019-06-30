#write a program that computes teh factorial of a given number
#print results in a comma-separated sequence on a single line


def factorial(num):

	result = num


	while num >0:

		if num > 3:
			result=result*num-1
			print(str(result)+',', end=" ")
		elif  num>2:
			result=result*num-1
			print(str(result))

		num-=1

	return result



		


def main():

	test=8
	answer=factorial(test)

	print('\n The factorial of '+str(test) + ' is ' +str(answer))



main()
