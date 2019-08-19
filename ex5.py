name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_cm = height * 2.54
weight = 180 # lbs
weigth_in_kg = weight * 0.45359237
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} inches tall.")
print(f"He's {weigth_in_kg} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair}.")
print(f"His teeth are usually {teeth} depending on the coffee")

# This line is tricky, try to get it exactly right
total = age + height_in_cm + weigth_in_kg
print(f"If I add {age}, {height_in_cm}, and {weigth_in_kg} i get {total}.")
