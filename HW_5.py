#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.

num = int(input("Введите число: "))
exp = int(input("Введите степень, в которую нужно возвести число: "))
def exponention_nums(num, exp):
    if num == 0:
        return 0
    if exp == 1:
        return num
    return num * exponention_nums(num, exp - 1)
a_res = exponention_nums(num, exp)
print(a_res)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a_num = int(input("Введите число: "))
b_num = int(input("Введите второе число: "))

def sum_rec(a_num, b_num):
    if a_num == 0:
        return b_num
    if b_num == 0:
        return a_num
    return 0 + sum_rec(a_num + 1, b_num - 1)
b_res = sum_rec(a_num, b_num)
print(b_res)
