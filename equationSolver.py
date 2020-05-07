def subtract(number1,number2):
    return number1-number2


def divide(number1,number2):
    return number1/number2

def multpily(number1,number2):
    return number1*number2

def sum(number1,number2):
    return number1+number2

if __name__ == '__main__':
    number1=int(input("Enter your First number:"))
    number2=int(input("Enter your second number:"))
    print('Now Enter the operation you want on these numbers:')
    operation=input()
    if operation=='+':
        print(sum(number1,number2))
    elif operation=='-':
        print(subtract(number1,number2))
    elif operation=='*':
       print( multpily(number1,number2))
    else:
        print(divide(number1,number2))


