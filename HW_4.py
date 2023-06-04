# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def create_array(*args):
    array_elem = int(input("Введите количество элементов  множества: "))
    list_1 = []
    count = 0
    while count < array_elem:
        a = int(input("Введите элемент множества: "))
        list_1.append(a)
        count += 1
    return list_1
n_array = create_array()
m_array = create_array()
n_set = set(n_array)
m_set = set(m_array)
new_set = n_set.intersection(m_set)
new_list = list(new_set)
new_list.sort()
for i in new_list:
    print(i, end=" ")


