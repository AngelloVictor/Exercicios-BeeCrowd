a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a, b, c, d, e]
pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 != 0]
positivos = [num for num in lista if num > 0]
negativos = [num for num in lista if num < 0]


print(f"{len(pares)} valor(es) par(es)")
print(f"{len(impares)} valor(es) impar(es)")
print(f"{len(positivos)} valor(es) positivo(s)")
print(f"{len(negativos)} valor(es) negativo(s)")