# write an is_even function
# write has_evens function
# write a count_evens function
# get_evens
# sum_evens
# multiply_evens
# count_all_evens : count ALL the evens in a list of numbers (a list of lists)
# sum_all_evens : sum all the evens in a list of list of numbers
# function called first_word returns first word (as a string) in a string
# function called removeEvens that accepts a list and returns a list w/all orig # except evens removed
# Function called isPrime that returns whether the input number is prime
# functionnamed mode that takes in a sequence of numbers and returns the most commonly occurring number
# write a function called shout that takes in a string and returns the entire string uppercared

def is_even(data):
	if data % 2 == 0:
		return True
	else:
		return False

def has_evens(data):
	for number in data:
		if is_even(data) == True:
			return True
	return False

def count_evens(data):
	even_count = 0
	for number in data:
		if is_even(number) == True:
			even_count += 1
	return even_count

def get_evens(data):
	numlist = [0]
	for number in data:
		if is_even(number) == True:
			numlist.append(number)
	return numlist

def sum_evens(data):
	list_sum = 0
	for number in data:
		if is_even(number) == True:
			list_sum += number
	return list_sum

def multiply_events(data):
	list_result = 0
	for number in data:
		if is_even(number) == True:
			list_result *= number
	return list_result

def sum_all_evens(data):
	sum_result = 0
	for group in data:
		for number in group:
			if is_even(number) == True:
				sum_result += number
	return sum_result

def multiply_all_evens(data):
	product_result = 0
	for group in data:
		for number in group:
			if is_even(number) == True:
				product_result *= number
	return product_result

def first_word(data):
	data_string = str(data)
	splitted = data_string.split()
	first = splitted[0]
	return first
#	return data_string.slice[:1]

def removeEvens(data):
	numlist = []
	for number in data:
		if is_even(number) == False:
			numlist.append(number)
	return numlist

def isPrime(data):
	if data >= 1:
		for number in range(2,data):
			if data % number == 0:
				return False
		return True

def mode(data):
	return max(set(data), key=data.count)
	
def shout(data):
	return data.upper()

numbers = [1, 2, 3, 4, 5, 6]
string = "1233 45567890"
matrix = [[1,2,3], [4,5,6], [7,8,9]]
freq = [1,2,3,1,2,1,2,4,5,1,6,1]

print(shout("banana"))