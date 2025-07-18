# def hello_world(text):
#     print(text)
# hello_world("print")

# add_labdma = lambda a, b: a / b
# #print(add_labdma(5, 2))
# even = lambda x:"Положительное" if x  > 0 else "Отрицательно" if x < 0  else "Ноль" 
# print(even(int(input("ведите число:"))))
    





# f = lambda x: (exec('def g(y): return y + 1', globals()), (x))[1]
# print(f(5))  


# try: 
#     x = int(input("введите число: "))
#     print(10 / x)
# except ValueError:
#     print("введите число а не букву")
# except ZeroDivisionError:
#     print("на ноль не делится")
# else:
#     print("Ошибок небыло")
# finally:
#     print("этот код выполняется всегда")



def plush_mach(num1, action, num2):
    if action == "+":
        return num1 + num2
    elif action == "-":
        return num1 + num2
    elif action == "*":
        return num1 * num2
    elif action == "/":
        return num1 / num2
    
    
    
num1 = int(input("Ведите первое число:"))
action = input("Ведите действие :")
num2 = int(input("Ведите второе число:"))
print(plush_mach(num1, action, num2))
try: 
    x = "piush_mach"
except ValueError:
    print("введите число а не букву")
except ZeroDivisionError:
    print("на ноль не делится")
else:
    print("Ошибок небыло")
finally:
    print("этот код выполняется всегда")
