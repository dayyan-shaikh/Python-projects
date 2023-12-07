def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        print("Denominator cannot be zero")

def mod(x, y):
    return x % y

def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = input("Enter number to perform: ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number : "))
            if choice == '1':
                print(f'{num1} + {num2} = {add(num1, num2)}')
            elif choice == '2':
                print(f'{num1} - {num2} = {sub(num1, num2)}')
            elif choice == '3':
                print(f'{num1} * {num2} = {mul(num1, num2)}')
            elif choice == '4':
                result = div(num1, num2)
                if result is not None:
                    print(f'{num1} / {num2} = {result}')
            elif choice == '5':
                print(f'{num1} % {num2} = {mod(num1, num2)}')
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid number")

calculator()
