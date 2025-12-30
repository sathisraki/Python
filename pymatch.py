https://www.programiz.com/python-programming/online-compiler/

print("Modes are ADD, SUB, MUL, DIV")
mode=input("Enter the mode of Operation:")

def oper(mode,x,y):
    match mode:
        case "ADD":
            print("Addition:")
            print(x+y)
        case "SUB":
            print("Subtraction:")
            print(x-y)
        case "MUL":
            print("Multiplicatoin:")
            print(x*y)
        case "DIV":
            print("Division:")
            print(x*y)
        case _:
            print("Unknown operation")

oper(mode,10,5)
