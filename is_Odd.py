def is_Odd(number):
	if number % 2 == 0:
		print(number," is not odd.")
	else:
		print(number," is odd.")
	return()


number=input("Please enter a number:  ")
try:
	is_Odd(int(number))
except ValueError:
	print("That is not a number.")