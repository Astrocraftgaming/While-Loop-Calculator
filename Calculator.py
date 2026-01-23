import math
Operator = "0"
num1 = "0"
num2="0"
while num1 == "0":
    try:
        num1 = float(input("Enter the first number:"))
    except ValueError:
        print("Only give numbers please!")
while num2 == "0":
    try:
        num2 = float(input("Enter the second number(press 1 if you wanna find the square root):"))
    except ValueError:
        print("Only give numbers please!")
if num2==1:
        result = math.sqrt(num1)
        print(f"The result is {result}")
else:
 while Operator != "+" or "-" or "/" or "*":
    Operator = str(input("Enter the operator(+,-,/,*,%,^):"))
    if Operator == "+":
                result = num1+num2
                print(f"The result is {result}")
                break
    elif Operator == "-":
               result = num1-num2
               print(f"The result is {result}")
               break        
    elif Operator == "/":
        try:
            result=num1/num2
            print(f"The result is {result}")
            break
        except ZeroDivisionError:
            print("The result is ∞")
            break
    elif Operator == "*":
                result = num1 * num2
                print(f"The result is {result}")
                break
    elif Operator == "%":
                result = num1 % num2
                print(f"The result is {result}")
                break
            
    elif Operator == "^":
                 result = num1 ** num2
                 print(f"The result is {result}")
                 break
    else:
                print(f"{Operator} is not a valid operator")

