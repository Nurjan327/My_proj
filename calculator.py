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
   



# class Truck:
#     def __init__(self, name,transport_type, color="белый", weight=10000):
#         self.name = name
#         self.transport_type = "грузовик"
#         self.color = color
#         self.weight = weight

#         print(f"Тип транспорта: {self.transport_type}, модель: {self.name}, цвет: {self.color}, вес: {self.weight} кг")


# my_truck = Truck("Volvo FH", "красный", 12000)



class Human:
    def __init__(self, first_name, last_name, height):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height

    def __str__(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Рост: {self.height} см"


person = Human("Иван", "Иванович", 176)


print(person)
