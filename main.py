def main():
    dawg = input("Choose (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if dawg == "+":
        print(num1 + num2)
    elif dawg == "-":
        print(num1 - num2)
    elif dawg == "*":
        print(num1 * num2)
    elif dawg == "/":
        if num2 != 0:
            print(num1 / num2) 
        else:
                print("Error: Dividing by zero") 
    else:
        print("Invalid equation selected")
main()

