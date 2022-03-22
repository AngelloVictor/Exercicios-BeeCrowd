segundos = int(input())
hora = segundos // 3600
segundos %= 3600
minuto = segundos // 60
segundos %= 60
segundos = segundos %(24*3600)

print(f"{hora}:{minuto}:{segundos}")