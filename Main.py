import Calculator

def main():
	exitStatement = "Press Enter to exit program..."

	print("Plese select one of the following operations:")
	print("		1: Multiplication")
	print("		2: Addition")
	print("		3: Subtraction")
	print("		4: Exponentiation")

	operationIdx = input()
	print("\n")

	operation = None
	if operationIdx == "1":
		operation = Calculator.multiply
	elif operationIdx == "2":
		operation = Calculator.add
	elif operationIdx == "3":
		operation = Calculator.subtract
	elif operationIdx == "4":
		operation = Calculator.exponent
	else:
		print("Your input was invalid. Please restart the program and try again")
		print("\n")
		input(exitStatement)
		return

	print("Plese input your X value:")
	x = input()
	print("Plese input your Y value:")
	y = input()
	print("\n")

	try:
		x = int(x)
		y = int(y)
	except ValueError:
		print("Your input was invalid. Please restart the program and try again")
		print("\n")
		input(exitStatement)

	result = operation(x,y)
	print("Result: %d" %result)
	print("\n")
	input(exitStatement)


if __name__ == "__main__":
	main()