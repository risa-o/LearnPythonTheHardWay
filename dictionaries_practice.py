# Dictionaries practice

# Consider the following shopping_cart list of dictionaries

shopping_cart = {
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "pickles",
            "price": 3.99,
            "quantity": 2
        }
    ],
    "tax": .08
}

# Exercise 1: 
# Write a function named get_subtotal() that takes in the dictionary. The get_subtotal function needs to return the sum of all of the items times each of their quantity.
def get_subtotal(shopping_cart):
    amt = []
    for item in shopping_cart['items']:
        qty = int(item['quantity'])
        price = float(item['price'])
        item_cost = qty * price
        amt.append(item_cost)
    return sum(amt)

# Exercise 2:
# Write a function named get_total that takes in the dictionary shopping_carts. The get_total function should return the subtotal plus tax on the subtotal amount.
def get_total(shopping_cart):
    subtotal = get_subtotal(shopping_cart)
    total = subtotal + (subtotal * shopping_cart['tax'])
    total = format(total, '.2f')
    return total

x = get_total(shopping_cart)
print(x)
# Hint: shopping_cart["items"] returns the list of objects. Using a for loop, you can iterate through a list of dictionaries...
# Hint: shoppint_cart["tax"] returns the percentage for calculating the tax.
# Hint: shopping_cart["items"][0]["title"] returns "orange juice"
# Hint: shopping_cart["items"][1]["title"] returns "rice"