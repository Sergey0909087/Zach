# def fan(a, s):
#     if a > s:
#         print('a больше s')
#     else:
#         print('s больше a')
# fan(3, 4)

# <------------------------------------>

# circule = [-2, 3, 10]

# def func():
#     pass
#
# class Test:
#     pass
#
# print(type(5))
# print(type('a'))
# print(type(5.5))
# print(type(True))
# print(type([1, 2]))
# print(type((5, 4)))
# print(type({1, 4}))
# print(type({'a': 2}))
# print(type(Test))
# print(type(func))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self): #сылка на значения персонажа
       print('Hello')

    def __str__(self):
        return f'Menya zovut {self.name}'

# person1 = Person(name='Ivan', age=15)
# person2 = Person(name='Petr', age=17)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)
#
# print(person1)
# print(person2)

# class Transport:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#
#     def beep(self):
#         print('Beeep')
#
#
# class Car(Transport):
#     def __init__(self, speed, color, owner):
#         super().__init__(speed, color)
#         self.owner = owner
#
#     def say_owner(self):
#         print(f'Vladelets {self.owner}')
#
#     def beep(self):
#         print('Hello')
#
# # car1 = Car(speed=100, color='Yellow', owner='Vasya')
# # print(car1.speed)
# # print(car1.color)
# # print(car1.owner)
# # car1.beep()
# # car1.say_owner()
#
# class Bus(Transport):
#     def __init__(self, speed, color, seats):
#         super().__init__(speed, color)
#         self.seats = seats
#
#     def say_seats(self):
#         print(f'Kolichestvo mest {self.seats}')
#
# # bus1 = Bus(speed=60, color='Blue', seats=33)
# # bus1.beep()
# # bus1.say_seats()
#
# class SportCar(Car, Transport):
#     pass
#
# car1 = SportCar(100, 'Green', 'Sergey')
# car1.beep()
# car1.say_owner()


class Uchenik:
    def __init__(self, age, class_ucheniya, sredni_bal, tip_classa, name_uchenik):
        self.age = age
        self.class_ucheniya = class_ucheniya
        self.sredni_bal = sredni_bal
        self.tip_classa = tip_classa
        self.name_uchenik = name_uchenik

    def say_delaet_dz(self):
        print(f'Uchenik {self.name_uchenik} делает дамашку')
    def Hi(self):
        print('Привет')

Uchenik1 = Uchenik(11, 4, 11, 'gumanitari', 'Sanya' )
print(Uchenik1.age)
print(Uchenik1.class_ucheniya)
print(Uchenik1.sredni_bal)
Uchenik1.Hi()
print(Uchenik1.tip_classa)
Uchenik1.say_delaet_dz()