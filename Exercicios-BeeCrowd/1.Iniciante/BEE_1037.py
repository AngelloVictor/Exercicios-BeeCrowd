valor = float(input())
intervalos = [[0.0, 25.0], [25.0, 50.0], [50.0, 75.0], [75.0, 100.00]]

if valor < 0:
    print("Fora de intervalo")

for i in range(4):
    for j in range(1):
        if valor > intervalos[i][j] and valor <= intervalos[i][j + 1]:
            print(f"Intervalo [{intervalos[i][j]:.0f},{intervalos[i][j+1]:.0f}]")
            break
