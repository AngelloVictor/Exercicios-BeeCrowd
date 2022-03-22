import math

a, b, c = map(float, input().split())
delta = (b ** 2) - (4 * a * c)

if (delta < 0 or a == 0):
    print("Impossivel calcular")

else:
    delta = math.sqrt(delta)
    r1 = (-b + delta) / (2 * a)
    r2 = (-b - delta) / (2 * a)
    print(f'R1 = {r1:0.5f}\nR2 = {r2:0.5f}')
