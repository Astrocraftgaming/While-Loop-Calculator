import math
import os
import sys
Operator = "0"
num1 = "0"
num2="0"
restart = "0"
restartTimes = "0"
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
                     print("Cant Divide By Zero")
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
Cal = "0"    
while Cal != "0": 
    Cal = str(input("Want to Calculate another problem?(Y/n):"))
    if Cal == "Y":
        Calc()
    elif Cal == "n":
        print("Bye")
        break
    else:
        print("Enter a valid answer")
while result != 0 and restartTimes == "0":
    restart = str(input("Restart? [Y/N]").upper())
    if restart == "N":
        print("Will not restart.")
        break
    elif restart == "Y":
        print("Restarting...")
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        print("Invalid command.")
        restart = str(input("Restart? [Y/N]"))



