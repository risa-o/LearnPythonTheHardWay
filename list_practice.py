# # Exercise 1: Write the code necessary to sum up all of the odd integers between 1 and 100. 
# You may use a previously defined function. 
# Hint: you'll likely need to produce a list of numbers..
def sum_odds():
	number = 0
	num_sum = 0
	num_list = []

	while number < 100:
		if number % 2 != 0:
			num_sum += number
		number += 1

	return num_sum
print(sum_odds())

# Exercise 2. Write a function called get_even_number that will only ever return an even number. 
# Inside the function, you may use the input() function to collect user input. 
# Hint: What's a good way to run code over and over based on a condition?
def enter_only_evens():
	num_entered = input("Please enter a number:  ")
	num_entered = int(num_entered)
	if num_entered % 2 == 0:
		return num_entered
	else:
		return(enter_only_evens())

x = enter_only_evens()
print(x)

# Define a function named remove_all(list, value) that takes in two arguments. 
# The first argument should be an existing list and 
# the second argument should be a value you wish to remove from that list. Example: 
# bugs = ["mosquito", "ant", "scorpion", "ant", "ant", "mosquito", "typo", "type error"]
# remove_bugs("mosquito") returns ["scorpion", "ant", "ant", "typo", "type error"]