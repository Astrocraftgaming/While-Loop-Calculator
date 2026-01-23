import math
Operator = "0"
num1 = "0"
num2="0"
while num1 == "0":
    try:
        num1 = float(input("Enter the first number:"))
    except ValueError:
        print("Only give numbers please!")
while Operator != "+" or "-" or "/" or "*":
    Operator = str(input("Enter the operator(+,-,/,*,%,^,sqrt):"))
    if Operator == "+":
          while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")                 
              else:  
                  result = num1+float(num2)
                  print(f"The result is {result}")
                  break
          break
    elif Operator == "-":
        while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")   
              else:  
               result = num1-float(num2)
               print(f"The result is {result}")
               break
        break
    elif Operator == "/":
        while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")   
              else:  
                  try:
                     result=num1/float(num2)
                     print(f"The result is {result}")
                     break
                  except ZeroDivisionError:
                     print("The result is ∞")
                     break
        break
    elif Operator == "*":
        while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")   
              else:  
                result = num1 * float(num2)
                print(f"The result is {result}")
                break
        break
    elif Operator == "%":
        while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")   
              else:  
                result = num1 % float(num2)
                print(f"The result is {result}")
                break
        break
            
    elif Operator == "^":
        while num2 == "0":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")   
              else:  
                 result = num1 ** float(num2)
                 print(f"The result is {result}")
                 break
        break
             
    elif Operator == "sqrt":
                  result = math.sqrt(num1)
                  print(result)
                  break
    else:
                print(f"{Operator} is not a valid operator")



