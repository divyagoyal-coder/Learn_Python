# Positional Arguments
# def cal_area(width, length):
#     return f"W : {width}, L: {length}, Area:{length*width}"
# print(cal_area(2,4))


# Keyword Arguments (named arguments)
# def cal_sum(*, x, y):
#     return f"Sum of {x} and {y} is {x+y}"
# print(cal_sum(y=3,x=7))


# Default Arguments
# def get_Area(width,length,shape='rectangle'):
#     if shape == 'rectangle':
#         return f"Area of {shape} is {width*length}"
#     elif shape == 'rhombus':
#         return f"Area of {shape} is {width*length/2}"

# print(get_Area(4,5,'rhombus'))


# Variable Argument
# def get_Perimeter(*params, shape='rectangle'):
#     if shape == 'rectangle':
#         return f"Perimeter of {shape} is {2*(params[0]+params[1])}"
#     elif shape == 'square':
#         return f"Perimeter of {shape} is {4*params[0]}"
#     elif shape == 'circle':
#         return f"Perimeter of {shape} is {2*3.14*params[0]}"
#     elif shape == 'triangle':
#         return f"Perimeter of {shape} is {params[0]+params[1]+params[2]}"

# print(get_Perimeter(7,shape="circle"))
# print(get_Perimeter(7,3,2,shape="triangle"))
# print(get_Perimeter(10,shape="square"))
# print(get_Perimeter(17,2))


# Keyword Variable Arguments (kwargs)
# def master_func(*, name ,**kwargs): 
#     return f"name = {name}, kwargs = {kwargs}"

# print(master_func(age=12, grade = 4, name="Siya", active = True, section = 'B', subjects = ['CPP', 'Java', 'Maths']))


