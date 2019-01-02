# Assign the following string to a variable named sales_string. "Monthly Sales Report\nDate: 03-17-2015\nOffice: Home Office\n ===================================================\nEmployee Number, First Name, Last Name, Sales Units\n***************************************************\n\n1, Jane, Janeway, 3\n3, Tricia, Triciason, 5\n4, Jeannette, Jeanson, 4\n5, Charles Emmerson III, Winchester, 2\n6, Chet, Chedderson, 8\n7, Chaiam, Chaiamson, 12\n8, Dale, Dalesinger, 1\n9, Zig, Ziglar, 50\n10, Henry, Kissinger, 1\n11, Arthur Herbert, Fonzarelli, 23\n12, Betty, Boop, 67". Now, write a function named sales_report() that takes in the sales_string as an argument. 

# xxxxNow write a function named sales_report() that takes in this string as its input.
sales_string = "Monthly Sales Report\nDate: 03-17-2015\nOffice: Home Office\n ===================================================\nEmployee Number, First Name, Last Name, Sales Units\n***************************************************\n\n1, Jane, Janeway, 3\n3, Tricia, Triciason, 5\n4, Jeannette, Jeanson, 4\n5, Charles Emmerson III, Winchester, 2\n6, Chet, Chedderson, 8\n7, Chaiam, Chaiamson, 12\n8, Dale, Dalesinger, 1\n9, Zig, Ziglar, 50\n10, Henry, Kissinger, 1\n11, Arthur Herbert, Fonzarelli, 23\n12, Betty, Boop, 67"

sales_list = sales_string.split('\n')
sales_ppl_list = sales_list[7:]
# The sales_report will be returning a dictionary with the following keys
# xxxxnumber_of_employees is a key that returns a value containing the number of employees
employee_number = len(sales_ppl_list)
# xxxxtotal_units_sold is a sum of all units sold by this sales team

def total_units_sold(sales_ppl_list):
	total = 0
	for person in sales_ppl_list:
		sales_detail = person.split(',')
		units_sold = sales_detail[3]
		total += int(units_sold)
	return total 

total = total_units_sold(sales_ppl_list)
# xxxxaverage units sold per employee is the total units sold divided by number of employees.
avg_sales = total / len(sales_ppl_list)
# most_units is a key that points to the name of the highest performing salesperson
# least_units is a key that points to the name of the lowest performing salesperson


# date_string = str(sales_list[1])
# date_list = date_string.split(': ')

	
output = {}
output["number_of_employees"] = employee_number
output['total_units_sold'] = total
output['average_units_sold'] = avg_sales
#output['most_units'] = 

print (output)
# Hint: this input is a CSV format, like a spreadsheet! 
# Since a CSV is two dimensional data, recommend splitting the original string to produce a list of strings.
# To identify the "delimeter", focus on which character separates each "row" of data.
# Some rows contain only formatting characters. Ignore or delete these rows.
# This list of strings contains the rows of data where each row is a full string containing all values.
# The first string of the list of strings should be "Monthly Sales Report". The next should be the Date, etc...
# Consider that each "row" may need to be split by another delimeter to access each field.