# Python has several types

"""
    Python has several types, but you don't need to know what type of variable it is
    Python can change the type on its variables
"""

name = 'Armando'
age = 40
height = 1.74
weight = 70
profession = "Data Engineer"

"""
    It's possible create data structures with the variables
"""
personal_list = [name, age, height, profession]
personal_tuple = (name, age, height, profession)
personal_dict = {"name": name, "age": age, "height": height, "profession": profession}
personal_set = {name, age, height, profession}

print(f"Hi {name}, how do you feel for your {age}th birthday?"
       "\nI feel very good, I have started exercising"
      f"\nand my height and my weight are {height} m and {weight} kg."
      f"\nBy the way I'm studing a {profession} course.\n")

print(f"The list is: {personal_list}")
print(f"The tuple is: {personal_tuple}")
print(f"The dictionary is: {personal_dict}")
print(f"The set is: {personal_set}")

# New values and types in variables and data structure
age = 'Armando'
profession = 40
name = 1.74
height = "Data Engineer"

personal_dict = {"name": name, "age": age, "height": height, "profession": profession}

print(f"\nThe new dictionary with the new values is: {personal_dict}")

