def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, z):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == "q":
            print("Goodbye !!")
            break

        if choice in("1","2","3","4"):
            try:
                num1 = float(input("Enter first Number: "))
                num2 = float(input("Enter second Number: "))
            except ValueError:
                print("Invalid Input. Please Enter Numbers only.")

            if choice == "1":
                print(add(num1, num2))
            elif choice == "2":
                print(subtract(num1, num2))
            elif choice == "3":
                print(multiply(num1, num2))
            elif choice == "4":
                 print(divide(num1, num2))

if __name__ == "__main__":
    calculator()