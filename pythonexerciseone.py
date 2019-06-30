#Question 1, Level 1
#Write a program which will find all numbers that are divisible by 7 butnot a multiple of 5
#between 2000 & 3000 inclusive

def practice(num1, num2):

	beg = num1
	end=num2+1

	keep = []

	for x in range(beg, end):

		if x%7 == 0 and x%5 != 0:

			 keep.append(x)
	return keep 



def main():

	result=[practice(2000,3000)]


	print(result)


main() 






