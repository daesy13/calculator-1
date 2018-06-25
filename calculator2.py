#Calculator 2

from arithmetic import *

def calculator_repl():
	while True:
		user_input = input("> ")
		user_list = user_input.split(" ")

		if user_input == "q": #quit if q is entered
			print("Exit")
			break
		elif len(user_list) < 2:
			print("Not Enough Inputs") #validate that at least 2 inputs are entered
			continue

		token = user_list[0]
		num1 = user_list[1]

		if len(user_list) < 3:
			num2 = "0"
		else:
			num2 = user_list[2]

		if len(user_list) < 4: 
			num3 = "0"
		else:
			num3 = user_list[3]

		is_digits(token, num1,num2,num3)

def calculate(token,num1,num2,num3):
	result = None
	if token == "+":
		result = add(num1, num2)

	elif token == "-":
		result = subtract(num1, num2)

	elif token == "*":
		result = multiply(num1,num2)

	elif token == "/":
		result = divide(num1, num2)

	elif token == "square":
		result = square(num1)

	elif token == "cube":
		result = cube(num1)

	elif token == "pow":
		result = power(num1, num2)

	elif token == "mod":
		result = mod(num1, num2)

	elif token == "x+":
		result = add_mult(num1, num2, num3)

	elif token == "cubes+":
		result = add_cubes(num1, num2)

	else:
		result = "Please enter an operator followed by two integers."

	print(result)

def is_digits(token,num1,num2,num3):
	if not num1.isdigit() or not num2.isdigit() or not num3.isdigit():
		print("those arent numbers")
		return
	else:
		calculate(token, float(num1),float(num2),float(num3))


calculator_repl()








