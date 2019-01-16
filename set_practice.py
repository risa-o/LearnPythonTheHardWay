fruits = ['kiwi', 'mango', 'tomato', 'mango', 'piña', 'sandia']

vegetables = ['eggplant', 'tomato', 'parsnips', 'turnips', 'onions', 'turnips', 'turnips', 'turnips', 'turnips']

# Demonstration
# making a set out of a list
# Notice that sets contain no duplicates.
bunchaNumbers = [1, 2, 3, 3, 3, 3, 4, 5, 1, 1, 6, 2]
setOfNumbers = set(bunchaNumbers)
print(setOfNumbers)

# Exercise 0
# Run set("banana") and observe the results. Then run set("mango") 
# and compare the differences.

# Exercise 1
# Reassign the fruits variable to be a set of the values that 
# fruits used to be. 

# Exercise 2 
# Reassign vegetables variable to be a set of the values that 
# vegetables used to be

# Exercise 3
# Add "banana" to the fruits set. Print your results. 
# Then try adding "banana" to the fruits set two more times. What do you see?

# Exercise 4
# Perform a union on the fruits and vegetables sets. 
# Store it to a variable named union_of_both

# Exercise 5
# Make an intersection of the fruits and vegetables sets. 
# Store it to a variable named intersection_of_both

# Exercise 6
# Perform a .difference of fruits on vegetables. 
# Example: set([1, 2, 3]).difference(set([3, 4, 5])) gives us {1, 2}

# Exercise 7
# Perform a .difference of vegetables on fruits. 
# Example: set([3, 4, 5]).difference(set([1, 2, 3])) gives us {4, 5}