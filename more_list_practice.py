# # Create a new python file named more_list_practice.py

# # Write a function called second that takes in a sequence and returns the second element in the sequence. 
# Example: second("banana") returns "a", second([4, 5, 6]) returns 5.
def second(seq):
	return seq[1]

# # Write a function called third that takes in a sequence and returns the third element in the sequence. 
# Example: third("banana") returns "n", third([4, 5, 6]) returns 6.
def third(seq):
	return seq[2]

# # Write a function named first_two that takes in a sequence and returns the first two elements in that sequence. 
# Eample first_two("banana") returns "ba", first_two([6, 7, 8]) returns [6, 7]. If the sequence only has one element, return the one element.
def first_two(seq):
	return seq[:2]

# # Write a function named first_three that takes in a sequence and returns the first three elements of that sequence. 
# Example first_three([9, 8, 7, 6, 5]) returns [9, 8, 7]
def first_three(seq):
	return seq[:3]

# # Write a function named last that takes in a sequence and returns the last and final element in the sequence. 
# Example: last([5, 6, 7]) returns 7
def last(seq):
	return seq[-1]

# # Write a function named second_to_last that takes in a sequence and returns the second to the last element. 
# Example second_to_last([6, 7, 8, 9]) returns 8
def second_to_last(seq):
	return seq[-2]

# # Write a function named third_to_last that takes in a sequence and returns the third to the last element. 
# Example third_to_last([6, 7, 8, 9]) returns 7
def third_to_last(seq):
	return seq[-3]

# # Write a function named last_two that returns the last two elements in a sequence. 
# Example last_two([5, 56, 7]) returns [56, 7]. If the list is of length two or less, return the entire list. 
def last_two(seq):
	if len(seq) > 2:
		return seq[-2:]

# # Write a function named last_three that returns the last 3 elements of a sequence. 
# Example last_three([7, 6, 5, 2, 1]) returns [5, 2, 1]. If the sequence is less than 3 elements long, return the entire list.

def last_three(seq):
	if len(seq) > 3:
		return seq[-3:]
