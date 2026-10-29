# sccm4910 lab project: 4 operation calculator
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def main():
	again = True
	while again == True:
		num1 = float(input("enter first number: "))
		operator = input("operator: ")
		num2 = float(input("enter second number: "))
		if operator == "+":
			print("result:", add(num1, num2))
		elif operator == "-":
			print("result:", subtract(num1, num2))
		elif operator == "*":
			print("result:", multiply(num1, num2))
		elif operator == "/":
			print("result:", divide(num1, num2))
		else:
			print("unknown operator:", operator)
		choice = input("quit? y/n: ")
		if choice == "y":
			again = False

if __name__ == "__main__":
	main()
