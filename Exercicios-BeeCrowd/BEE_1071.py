x = int(input())
y = int(input())

impares = []
for i in range(y + 1, x):
    if i % 2 != 0:
        impares.append(i)


print(impares)
print(sum(impares))
