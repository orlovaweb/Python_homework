# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def func(a, b):
    if b == 0:
        return 1
    return a*func(a, b-1)


print(func(int(input("A = ")), int(input("B = "))))
