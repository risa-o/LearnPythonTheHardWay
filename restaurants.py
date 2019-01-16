# Given the following variables, return a list of restaraunt entries 
# that are open at that day/time.

import requests
import random

url = "https://frest.glitch.me/restaurants"

response = requests.get(url)

data = response.json()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
random_am_pm = random.choice(["am", "pm"])
random_day_of_week = random.choice(days)
random_hour = random.choice(list(range(1, 12)))
random_minute = random.choice(list(range(1, 60)))

# restaurant_names = []
# for restaurant in data:
# 	name = restaurant['name']
# 	restaurant_names.append(name)

# for restaurant in data:
# 	times = restaurant[]


print (data)

