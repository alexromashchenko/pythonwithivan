#EASY

# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

# a = 15
# b = 27.3
# c = 'Приветствую,'
# name = input('Как Вас зовут?')
# print(c, name)


# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# chislo = float(input('Введите число'))
# chislo = chislo + 2
# print(chislo)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# vozr = float(input('Какой Ваш возраст?'))
# if vozr >= 18:
#     print("Доступ разрешен")
# else:
#     print('Извините, пользование данным ресурсом только с 18 лет')


#NORMAL

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

# chis = int(input('Введите число'))
# while chis < 0 or chis >= 10:
#     print('Введенное число должно быть целым и в диапазоне от 0 и до 10')
#     chis = int(input('Введите число'))
# chis = chis ** 2
# print(chis)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

# a = input("введите число a")
# b = input("введите число b")
# print('По заданным параметрам, число a = ', a + ', число b = ', b)
# print('Теперь поменяем их местами')
# a, b = b, a
# print("Теперь значение а = ", a + ", значение b = ", b)


#HARD

# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

# name = input('Введите свое имя и фамилию')
# age = int(input("Введите свой возраст"))
# weight = int(input('Введите свой вес в килограммах'))
# if age < 30 and (weight > 50 and weight < 120):
#     print("Хорошее состояние")
# elif age >=30 and (weight < 50 or weight > 120):
#     print('Требуется начать вести правильный образ жизни')
# elif age > 40 and (weight < 50 or weight > 120):
#     print("Требуется врачебный осмотр")
# else:
#     print('Вы какой-то нестандартный, программа на Вас не рассчитана...')

#Конец первого урока)))
