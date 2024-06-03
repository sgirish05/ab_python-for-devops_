import sys
print("Enter two numbers and operation: add,sub,mul,div in format:python calclulator.py 10 7 div")
def add(num1, num2):
    sum = num1 + num2
    return sum
def sub(num1, num2):
    sub = num1 - num2
    return sub
   # print("Subtraction result is ", sub)
def mul(num1, num2):
    mul =num1 * num2
    return mul
def div(num1, num2):
    div = num1 // num2
    return div

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]
if operation == "add":
    output = add(num1, num2)
    print(output)
if operation == "sub":
    output = sub(num1, num2)
    print(output)
if operation == "mul":
    output = mul(num1, num2)
    print(output)
if operation == "div":
    output = div(num1, num2)
    print(output)
