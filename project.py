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



# def plush_mach(num1, action, num2):
#     if action == "+":
#         return num1 + num2
#     elif action == "-":
#         return num1 + num2
#     elif action == "*":
#         return num1 * num2
#     elif action == "/":
#         return num1 / num2
    
    
    
# num1 = int(input("Ведите первое число:"))
# action = input("Ведите действие :")
# num2 = int(input("Ведите второе число:"))
# print(plush_mach(num1, action, num2))
# try: 
#     x = "piush_mach"
# except ValueError:
#     print("введите число а не букву")
# except ZeroDivisionError:
#     print("на ноль не делится")
# else:
#     print("Ошибок небыло")
# finally:
#     print("этот код выполняется всегда")



# file = open("text.txt", "w")
# file.write("Бекнден самый лучший")
# file.close()

# file = open("text.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("Nurjan.txt", 'w') as f:
#     f.write("салам Нуржан\n")
#     f.write("это вторая строка\n")

# with open("Nurjan.txt", 'r') as f:
#     data = f.read()
#     print(data)





file_name = input("Введите имя файла (например, notes.txt): ")

with open(file_name, "w") as f:
    for i in range(3):
        line = input(f"Введите строку {i + 1}: ")
        f.write(line + "n")

print("n Содержимое файла:")
with open(file_name, "r") as f:
    for line in f:
        print(line.strip())

