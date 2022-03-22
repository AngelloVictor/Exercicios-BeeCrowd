horas = list(map(int, input().split()))

if (horas[0] == 0 and horas[1] == 0) or (horas[0] == horas[1]):
    print("O JOGO DUROU 24 HORA(S)")
    
elif horas[0] > horas[1]:
    print(f"O JOGO DUROU {24-horas[0]+horas[1]} HORA(S)")
    
elif horas[0] < horas[1]:
    print(f"O JOGO DUROU {abs(horas[0]-horas[1])} HORA(S)")
    