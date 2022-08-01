p1, p2 = list(map(float, input().split()))

if p1 == 0 and p2 == 0:
    print("Origem")

elif p1 == 0:
    print("Eixo X")

elif p2 == 0:
    print("Eixo Y")

elif p1 > 0 and p2 > 0:
    print("Q1")

elif p1 < 0 and p2 > 0:
    print("Q2")

elif p1 < 0 and p2 < 0:
    print("Q3")

elif p1 > 0 and p2 < 0:
    print("Q4")
