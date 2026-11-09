import math

Operator = None
running= True
num1=None
Operators = ("+","-","/","*","%","^","sqrt")
def Calc():
 global num1
#Entering 1st number
 while num1==None:
  try:
    num1 = float(input("Enter the first number:"))
  except ValueError:
    print("Only give numbers please!")
 global Operator
 #Entering operator
 while Operator not in Operators :
    Operator = input("Enter the operator(+,-,/,*,%,^,sqrt):")
    if Operator not in Operators:
        print("Enter a proper operator")
 while running:
     match Operator:
#Adding
        case "+":
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
                      num1 = None
                      break
    #Subtracting
        case "-":
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
                   num1 = None
                   break
    #Dividing
        case "/":
                  try:
                    num2 = float(input("Enter the second number:"))
                  except ValueError:
                      print("Only Enter Numbers please!")
                  except TypeError:
                      print("Only Enter Numbers please!")
                  except ZeroDivisionError:
                      print("Cant Divide By Zero")
                      Operator = "0"
                      num1 = None
                      break
                  else:
                      result=num1/float(num2)
                      print(f"The result is {result}")
                      Operator = "0"
                      num1 = None
                      break
    #Multiplying
        case "*":
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
                    num1 = None
                    break
    #Calculation of modulus
        case "%":
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
                     num1 = None
                     break
    #Calculations of power
        case "^":
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
                     num1 = None
                     break
    #square root calculations
        case "sqrt":
                      result = math.sqrt(num1)
                      print(result)
                      Operator = "0"
                      num1 = None
                      break
#Restart the calculator
Calc()
while running:
    restart = input("Do you want to calculate another equation?(y/n):").lower()
    match restart:
        case "y":
            Calc()
        case "n":
            print("Thank you for using the calculator")
            running=False
        case _:
            print("You entered an invalid option, try again")

