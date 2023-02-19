number = input("Введите номер билетика: ")
leftPart = int(number[0])+int(number[1])+int(number[2])
rightPart = int(number[3])+int(number[4])+int(number[5])
print("Счастливый" if leftPart == rightPart else "Не является счастливым")
