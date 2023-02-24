n = int(input("Введите потолок для значений степеней двойки: "))
i = 1
while (pow := 2**i) < n:
    print(pow)
    i += 1
