# class Car:
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand
#
#
# hilux=Car('blue','toyota')
# print(hilux.color)

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
# acc = BankAccount(100)
# acc.deposit(50)
# acc.withdraw(30)
# print(acc.balance)


# class Color:
#     def __init__(self, name):
#         self.name = name
# c1 = Color("red")
# c2 = Color("blue")
# # c1.name = "green"
# print(c1.name, c2.name)


# exe1


class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f'{self.name} says woof')

# rex=Dog('rex')
# print(rex.name)
# rex.bark()
# Dog('rex').bark()



# exe2

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height


# print(Rectangle(3,4).area())



# exe3


class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1

    def value(self):
        print(self.count)

# c=Counter()
# c.increment()
# c.increment()
# c.value()


# exe4

class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f'{self.a},{self.b}'

# p=Point(1,2)
# print(p)



# exe5

class BankAcoount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print('error')
        else:
         self.balance-=amount

# my_count=BankAcoount()
# my_count.withdraw(30)
# print(my_count.balance)
# my_count.deposit(50)
# my_count.withdraw(20)
# print(my_count.balance)




# exe6

class Temperature:
    def __init__(self,temp):
        self.temp=temp
    def to_fahrenheit(self):
        return self.temp*1.8+32
# print(Temperature(34).to_fahrenheit())

# exe7

class Student:
    school='Kodcode'
    def __init__(self,name):
        self.name=name

# a=Student('moty')
# b=Student('avi')
#
# a.name='yakov'
# print(a.school,a.name)
# print(b.school,b.name)




# exe8

class Player:
    count=0
    def __init__(self,name):
        self.name=name
        Player.count+=1


# a=Player('a')
# b=Player('b')
# b.count=9
# print(b.count)
# print(Player.count)



# exe9

class Money:
    def __init__(self,amount=35):
        self.amount=amount
    def is_more_than(self,other):
        return f'{self.amount} are {self.amount-other.amount} more than {other.amount}'

# a=Money(30)
# b=Money(10)
# print(a.is_more_than(b))


# exe10

class PlayList:
    def __init__(self):
        self.list_song=[]

    def add(self,title):
        self.list_song.append(title)
    def remove(self,title):
        self.list_song.remove(title)
    def count(self):
        print(len(self.list_song))
    def __str__(self):
        return f'{self.list_song}'


a=PlayList()
a.add('asd')
a.add('asd')
# a.remove('asd')
a.count()
print(a)