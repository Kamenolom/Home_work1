Задание1

num1 = int(input("Введите число которое будет возведено в квадрат:"))
num2 = 2
result = num1 ** num2
print("Квадрат числа:" , result)

Задание2

num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
num3 = int(input("Введите  третье число:"))
result = (num1 + num2 + num3) // 3
print(result)

Задание3

minutes = int(input("Введите количество минут:"))
hours = minutes // 60
minutes2 = minutes % 60
print(hours ,"Часов" ,  minutes2 , "Минут")

Задание4

price = float(input("Введите сумму товара:"))
discount = float(input("Введите процент скидки:"))
discount2 =price * discount / 100 #1000*15/100= 15000/100=150
final_price = price - discount2 #1000-150=850
print(final_price)

Задание5

number = int(input("Введите 3-х значное число,в котором будет выведена последняя цифра:"))
n1 = number % 10
print(n1)

Задание6

a = int(input("Введите длину прямоугольника:"))
b = int(input("Введите ширину прямоугольника:"))
perimetr = (diagonal1 + diagonal2) *2
print("Периметр:" ,perimetr)

Задание7

number = int(input("Введите 4-х значное число:"))
n1 = number //1000 #4
n2 = number %1000 //100
n3 = number %100 //10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)


























