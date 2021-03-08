def addition (num1 , num2):
    return float(num1) + float(num2)

def substraction (num1, num2):
    return float(num1) - float(num2)

def division (num1, num2):
    return float(num1) / float(num2)

def multiplication (num1, num2):
    return float(num1) * float(num2)
    

num1 = input("Please input first number: ")
num2 = input("Please input second number: ")
fun = int(input("Please input 1 for additon, \n input 2 for substraction, \n input 3 for division, \n or input 4 for multiplication :"))

if fun == 1 :
    print('The sum is ' + str(addition(num1,num2)))
elif fun == 2:
    print('The difference is ' + str(substraction(num1,num2)))
elif fun == 3:
    print('The division result is ' + str(division(num1,num2)))
else:
    print('The multiplication result is ' + str(multiplication(num1,num2)))