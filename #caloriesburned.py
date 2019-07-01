#caloriesburned.py

#header
CALORIESPERMINUTE = 4.2
print('Minutes\t\tCalories Burned')
print('-------------------------------')
total=0
for time in range(10,31,5):
	total=time*CALORIESPERMINUTE

	print(time,'\t\t',total)


