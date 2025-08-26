def add(n1 , n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def mul(n1 , n2):
    return n1 * n2
def div(n1 , n2):
    return n1 / n2
def mod(n1 , n2):
    return n1 % n2
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
sel = input("Enter operation + , - , * , / , % : ")

if sel == '+':
    print(n1 , "+" , n2 , "=",add(n1 , n2))
elif sel == '-':
    print(n1 , "-" , n2 , "=",sub(n1 , n2)) 
elif sel == '*':
    print(n1 , "*" , n2 , "=",mul(n1 , n2))
elif sel == '/':
    print(n1 , "/" , n2 , "=",div(n1 , n2))
elif sel == '%':
    print(n1 , "%" , n2 , "=",mod(n1 , n2))
else :
    print("Invalid operation")

