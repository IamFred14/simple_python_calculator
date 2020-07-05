# Function definition for the math operations.

def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mult(num1,num2):
    print(num1*num2)
def div(num1,num2):
  try:
      print(num1/num2)
  except ZeroDivisionError as err:
      print(err)

# Defining a boolean exit button.
leave = False
# while loop in function to our boolean button
while leave == False :
  
    # Getting input from the user(The input starts all as str but is converted to float after).
    try:
      numA, oper, numB = input("Ready: ").split()
    except ValueError as err:
      print(err)
      break
    
    num1, num2 = float(numA), float(numB)
  

    #conditionals for the final result.

    if oper == "+":
      add(num1, num2)
    elif oper == "-":
      sub(num1,num2)
    elif oper == "x" or oper == "*":
      mult(num1,num2)
    elif oper== "/":
      div(num1,num2)
    else:
      print("Invalid operator, please try again!")

    get_out = input("Type exit if you wish to leave, or press enter to continue")
    if get_out == "exit" or get_out == "Exit":
      leave = True
    else :
      leave = False

   
