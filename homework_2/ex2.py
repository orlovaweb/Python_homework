x = int(input())
y = int(input())
for i in range(1000):
    for j in range(1000):
        if i+j == x and i*j == y:
            print(i, j)
