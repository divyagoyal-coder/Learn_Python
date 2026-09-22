# FUNCTIONS
# def get_updates():
#     return "Getting Updates..."

# print(get_updates())

# __________________________________________________________
#Positional Argument : width, length, Default Argument : shape
# def get_area(width, length, shape="rectangle"):   
#     return f"Area of {shape} is {width * length}"

# print(get_area(12, 12, 'square'))

# __________________________________________________________
# Variable Arguments
# def get_shopping_List(*args, basket="Copper"):
#     return args

# print(get_shopping_List("apple", "mango", "berries"))
# print(get_shopping_List(1,2,['purple','red']))

# __________________________________________________________
# Keyword Arguments (Named Arguments)
# def get_Reward(*, first, second, third):
#     return f"1: {first}, 2: {second}, 3: {third}"

# print(get_Reward(third="Rahul", first = "Uma", second = "Ikra"))

# __________________________________________________________
# Keyword Variable Arguments
# def super_function(*, name, age, **data):
#     return data

# print(super_function(cars='5 BMWs', house = 3,name="Priyansh", jet=1, age= 12, fruit='apple', active=True))


# __________________________________________________________
# import time

# # DECORATORS
# def time_elapsed(callback):
#     start = time.time()
#     callback()
#     end = time.time()

#     return print(f"Time taken to execute is {end-start}")

# @time_elapsed
# def greeting():
#     print("Welcome Champs")

# @time_elapsed
# def call_area():
#     print(f"Area is being calculated here")