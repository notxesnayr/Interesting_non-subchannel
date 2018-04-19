def add(a,b):
       return a+b
def subtraction(a,b):
       return a-b
def multiplication(a,b):
       return a*b
def division(a,b):
       return a/b
def exponential(a,b):
       return a**b
def factorial(a):
    if a >= 0:    
        if a == 1 or 0:
            return 1
        else:
            return a * factorial(a-1)
    else:
        if a == -1:
            return -1
        else:
            b = -a
            if b > 1:
                return -(b * factorial(b-1))
print(' 1.add\n','2.subtraction\n','3.multiplication\n','4.division\n','5.exponential\n','6.factorial')
choice = input("Enter Desired Operation (1-6):")
if choice == '1' or choice == '2' or choice =='3' or choice =='4' or choice =='5' or choice =='6':    
    num1 = int(input('Enter the first number'))
    
    if choice != '6':  
        num2 = int(input('Enter the second number'))
    if choice == '1':
        print('\n',num1, '+', num2, '=', add(num1,num2))
    elif choice == '2':
        print('\n',num1, '-', num2, '=', subtraction(num1,num2))
    elif choice == '3':
        print('\n',num1, '*', num2, '=', multiplication(num1,num2))
    elif choice == '4':
        print('\n',num1, '/', num2, '=', division(num1,num2))
    elif choice == '5':
        print('\n',num1, '^', num2, '=', exponential(num1,num2))
    elif choice == '6':
        if num1==1:
            print(num1,'!','=',1)
        else:
            print(num1,'!','=',factorial(num1))
else: print("INCORRECT CHOICE")
    