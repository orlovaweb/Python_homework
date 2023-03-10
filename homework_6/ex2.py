import random
n = int(input("Введите количество элементов массива: "))
min = int(input("Введите минимум отрезка: "))
max = int(input("Введите максимум отрезка: "))

lst = [random.randrange(30) for _ in range(n)]
print(lst)
for i in range(n):
    if min <= lst[i] <= max:
        print(i, end=" ")
