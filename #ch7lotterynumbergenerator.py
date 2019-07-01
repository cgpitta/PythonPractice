#ch7lotterynumbergenerator.py

import random
lotto_list=[]

for num in range(7):
	lotto_list.append(random.randint(0,9))

for val in lotto_list:
	print('The lottory number is: ',val)
