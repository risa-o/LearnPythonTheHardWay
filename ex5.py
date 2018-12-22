name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #Inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
pounds_in_a_kilogram = 2.20
height_in_centimeters = height * 2.54
weight_in_kilograms = weight / 2.20
rounded_weight_in_kilograms = round(weight_in_kilograms)

print(f"My height in centimeters is {height_in_centimeters} and my weight in kilograms is {rounded_weight_in_kilograms}.")