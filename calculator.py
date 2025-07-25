# def plush_mach(num1, action, num2):
#     if action == "+":
#         return num1 + num2
#     elif action == "-":
#         return num1 + num2
#     elif action == "*":
#         return num1 * num2
#     elif action == "/":
#         return num1 / num2
#     else :
#         return"На ноль не делится."
    
# num1 = int(input("Ведите первое число:"))
# action = input("Ведите действие :")
# num2 = int(input("Ведите второе число:"))
# print(plush_mach(num1, action, num2))
   



class Truck:
    def __init__(self, name, color="белый", weight=10000):
        self.name = name
        self.transport_type = "грузовик"
        self.color = color
        self.weight = weight

        print(f"Тип транспорта: {self.transport_type}, модель: {self.name}, цвет: {self.color}, вес: {self.weight} кг")


my_truck = Truck("Volvo FH", "красный", 12000)



