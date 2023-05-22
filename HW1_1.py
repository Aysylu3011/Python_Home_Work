# 1.
# Найдите сумму цифр трехзначного числа.
num = int(input("Введите трехзначное число: "))
third_num = num % 10
new_num = num // 10
second_num = new_num % 10
first_num = num // 100
print(third_num + second_num + first_num)

# вариант с циклом

num_var2 = int(input("Введите трехзначное число: "))
sum = 0
while num_var2 > 0:
        f_num = num_var2 % 10
        sum = sum + f_num
        num_var2 = num_var2 // 10
print(sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


quantity_cranes = int(input("Введите количество журавликов: "))
part_of_boys = quantity_cranes // 6
if quantity_cranes >= 6:
        part_kate = (part_of_boys + part_of_boys) * 2
        remainder = quantity_cranes - (2 * part_of_boys) - part_kate
        if remainder > 3:
                part_kate = part_kate + 3
                part_of_boys = part_of_boys + (remainder - 4)
                remainder = remainder - 4
        if remainder <= 3:
                part_kate = part_kate + remainder
                remainder = remainder - 3

        print("Петя и Сережа сделали по {} журавликов, Катя {}".format(part_of_boys, part_kate))
else:
        print("Число не подходит под условие задачи")


# Задача 6
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

number_of_ticket = int(input("Введите номер билета (6 цифр): "))
first_part = number_of_ticket // 1000
first_sum = 0
second_sum = 0
while number_of_ticket > 999:
        num_for_second_sum = number_of_ticket % 10
        second_sum = second_sum + num_for_second_sum
        number_of_ticket = number_of_ticket // 10
while first_part > 0:
        num_for_first_sum = first_part % 10
        first_sum = first_sum + num_for_first_sum
        first_part = first_part // 10
if first_sum == second_sum:
        print("Билет счастливый")
else:
        print("Самый обычный билет")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

parts = int(input("Введите количество долек: "))
size_m = int(input("Введите размер m: "))
size_n = int(input("Введите размер n: "))
n_fit = parts / size_m
m_fit = parts / size_n
if (parts % size_m == 0 and m_fit < size_n) or (parts % size_n == 0 and n_fit < size_m):
        print("От шоколадки {} на {} можно отделить {} долек за 1 разлом".format(size_m, size_n, parts))
else:
        print("От шоколадки {} на {} нельзя отделить {} долек за 1 разлом".format(size_m, size_n, parts))
