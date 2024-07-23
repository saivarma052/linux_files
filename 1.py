def is_calc(operation, n1, n2):
    if operation == 'add':
        return n1 + n2
    elif operation == 'sub':
        return n1 - n2
    elif operation == 'mul':
        return n1 * n2
    elif operation == 'div':
        if n2 != 0:
            return n1 / n2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

print("Select operation\n1.add\n2.sub\n3.mul\n4.div")
operation = input("Enter your operation (add/sub/mul/div): ").strip()
n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))

result = is_calc(operation, n1, n2)
print("Result of the selected operation: ", result)



