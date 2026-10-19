import math
Operator = None
running= True
num1=None
Operators = ("+","-","/","*","%","^","sqrt")
def Calc():
 global num1
#Entering 1st number
 while num1!=0:
  try:
    num1 = float(input("Enter the first number:"))
    break
  except ValueError:
    print("Only give numbers please!")
 global Operator
 #Entering operator
 while Operator not in Operators :
    Operator = input("Enter the operator(+,-,/,*,%,^,sqrt):")
 while running:
#Adding
    if Operator == "+":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")
              else:
                  result = num1+num2
                  print(f"The result is {result}")
                  Operator = "0"
                  break
#Subtracting
    elif Operator == "-":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")
              else:
               result = num1-float(num2)
               print(f"The result is {result}")
               Operator = "0"
               break
#Dividing
    elif Operator == "/":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")
              except ZeroDivisionError:
                  print("Cant Divide By Zero")
                  Operator = "0"
                  break
              else:
                  result=num1/float(num2)
                  print(f"The result is {result}")
                  Operator = "0"
                  break
#Multiplying
    elif Operator == "*":
              try:
                num2 = float(input("Enter the second number:"))
              except ValueError:
                  print("Only Enter Numbers please!")
              except TypeError:
                  print("Only Enter Numbers please!")
              else:
                result = num1 * float(num2)
                print(f"The result is {result}")
                Operator = "0"
                break
#Calculation of modulus
    elif Operator == "%":
                try:
                  num2 = float(input("Enter the second number:"))
                except ValueError:
                  print("Only Enter Numbers please!")
                except TypeError:
                  print("Only Enter Numbers please!")
                else:
                 result = num1 % float(num2)
                 print(f"The result is {result}")
                 Operator = "0"
                 break
#Calculations of power
    elif Operator == "^":
            try:
                num2 = float(input("Enter the second number:"))
            except ValueError:
                  print("Only Enter Numbers please!")
            except TypeError:
                  print("Only Enter Numbers please!")
            else:
                 result = num1 ** float(num2)
                 print(f"The result is {result}")
                 Operator = "0"
                 break
#square root calculations
    elif Operator == "sqrt":
                  result = math.sqrt(num1)
                  print(result)
                  Operator = "0"
                  break
#Restart the calculator
Calc()
while running:
    restart = input("Do you want to calculate another equation?(y/n):")
    if restart.lower()=="y":
        Calc()
    elif restart.lower()=="n":
        print("Thank you for using the calculator")
        running=False
    else:
        print("You entered an invalid option, try again")
