'''
Задача № 2. Проверить, является ли четырехзначное число палиндромом
Пример:
Вход: 1221  Выход: 1221 - палиндром
Вход: 1234  Выход: 1234 - не палиндром
'''
# а можно ли оставить str и передвигатьсся по строкам? или может через массив?
number = int(input('4-x number:'))

number_one = int(number / 1000)
number_two = int((number - number_one * 1000) / 100 )
number_three = int(number % 100 / 10)
number_four = int(number % 10)

if number_one == number_four and number_two == number_three:
    print('palindrom')
else: print('bad')
#print(number_one, number_two, number_three, number_four)