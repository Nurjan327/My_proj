def plush_mach(num1, action, num2):
    if action == "+":
        return num1 + num2
    elif action == "-":
        return num1 + num2
    elif action == "*":
        return num1 * num2
    elif action == "/":
        return num1 / num2
    else :
        return"На ноль не делится."
    
    
num1 = int(input("Ведите первое число:"))
action = input("Ведите действие :")
num2 = int(input("Ведите второе число:"))
print(plush_mach(num1, action, num2))
        