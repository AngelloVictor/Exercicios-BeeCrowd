a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a, b, c, d, e, f]
positivos = []

for numero in lista:
    if numero  > 0:
        positivos.append(numero)
        
print(f"{len(positivos)} valores positivos")
print("{:.1f}".format(sum(positivos)/len(positivos)))