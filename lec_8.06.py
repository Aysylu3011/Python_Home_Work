#list_a = [1, 2, 3, 4, 5, 8, 15, 23, 38]
#list_b = []
#for i in list_a:
#    if i % 2 == 0:
#        list_b.append((i, i** 2))

#print(list_b)

def select(f, col):
    return[f(x) for x in col]
def where(f, col):
    return[x for x in col if f(x)]
list_a = [1, 2, 3, 4, 5, 8, 15, 23, 38]
res = select(int, list_a)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
# функцимю select можно заменить на функцию map -
# это встроенная функция в питоне, а функцию where заменить на функцию filter

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
first_element = int(input("Введите первый элемент арифметической прогрессии: "))
amounts_elements = int(input("Введите количество элементов арифметической прогрессии: "))
d_of_progression = int(input("Введите разность арифметической прогрессии: "))
a = first_element + (amounts_elements - 1) * d_of_progression
list_1 = []
for i in range(first_element, a + 1, d_of_progression):
    list_1.append(i)
print(list_1)

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
start_element = int(input("Введите первый элемент: "))
finish_element = int(input("Введите второй элемент: "))
list_new = [x for x in range(1, 20)]
print(list_new)
for i in range(len(list_new)):
    if list_new[i] >= start_element and list_new[i] <= finish_element:
        print(i)
