# Error Function for Easy Use
def error(message):
    print("Error |", message)

#___________________________________
def percent(untotal, total):
    print(int(untotal) / int(total) * 100)

#__________________________________
def sum(op, a, b):
    if op in ("+", "-", "*", "/"):
        if op == "+":
            print(a + b)
        
        elif op == "-":
            print(a - b)
        
        elif op == "*":
            print(a * b)
        
        elif op == "/":
            if b == 0:
                error("Cannot Divide By Zero")
            
            else:
                print(a / b)
            
        
        else:
            error("Critical Error In Code {CHOOSING OPERATOR}")
        
    else:
        error("Operator is Not Valid")
    

#__________________________________
while True:
    print("___________________________________")
    print("Calculator")
    print("1 - Regular Math")
    print("2 - Percent Calculator")
    version = input("Type: ")
    if version == "1":
        op = input("Operator +, -, *, /: ")
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter Another Number: "))
        sum(op, num1, num2)
    
    elif version == "2":
        nontotal = input("Non-Total: ")
        total = input("Total: ")
        percent(nontotal, total)
    
    else:
        error("Type is not Valid")
    

#__________________________________
