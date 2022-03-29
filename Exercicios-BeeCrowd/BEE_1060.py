a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a, b, c, d, e, f]
positivos = []

for i in lista:
    if i > 0:
        positivos.append(i)
        
        
print(f"{len(positivos)} valores positivos")
