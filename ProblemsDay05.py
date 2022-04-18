# Assignment 1
# def nozero(func):
# 	def helper(*args):
# 		print("Logged into the service...")
# 		print(func(*args))
# 		print("Logged out the service...")
# 		print("-" * 40)
# 	return helper
#
# @nozero
# def div(x, y):
# 	return x/y
#
# @nozero
# def mul(x, y):
# 	return x*y
#
# @nozero
# def add(x, y):
# 	return x+y
#
# @nozero
# def sub(x, y):
# 	return x-y
#
# div(100, 50)
# mul(100, 50)
# sub(100, 50)
# add(100, 50)



# Assignment 2

# def drawborder(fnc1):
#     def helper(*args, **kwargs):
#         print("*" * 40)
#         fnc1(*args)
#         print("#" * 40)
#     return helper
#
# @drawborder       #('*','#', 40)
# def greet(msg):
#     print("Welcome ", msg)
#
# @drawborder       #('=','_', 30)
# def RSVP(msg):
#     print("Have a good day!", msg)
#
# greet("ankush")
# RSVP("ankush")



# Assignment 3

# def logBeforeAfter(fnc):
#     def helper(*args):
#         print("-" *40)
#         fnc(*args)
#     return helper

# @logBeforeAfter
# def fun(x, y):
#     print("fun", x, y)

# @logBeforeAfter
# def fun1(*args):
#     print("fun1", args[1])

# @logBeforeAfter
# def fun2(**kwargs):
#     print("fun2", kwargs)

# @logBeforeAfter
# def fun3(*args, **kwargs):
#     print("fun3", args, kwargs)

# logBeforeAfter(fun)
# fun(20,40)
# fun1("ankush", "rathore")
# fun2()
# fun3(9, 10)
