# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
n = int(input("Введите количество элементов массива: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)
x = int(input("Какое число искать: "))
count = 0
for i in lst:
    if i == x:
        count += 1
print(f"Встретилось {count} раз")
