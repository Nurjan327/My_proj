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



class Person:
    def __init__(self, name, surname, height):
        self.name = name
        self.surname = surname
        self.height = height

    def __str__(self):
        return f"{self.surname} {self.name}, рост: {self.height} см"


class Student(Person):
    def __init__(self, name, surname, height, class_level):
        super().__init__(name, surname, height)
        self.class_level = class_level

    def __str__(self):
        return f"{self.surname} {self.name}, рост: {self.height} см, учится в классе: {self.class_level} 10b"

my_student_person = Student("Иван", "Петров", 180, "10Б")
print(my_student_person)
