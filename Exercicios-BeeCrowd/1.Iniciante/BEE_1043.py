A,B,C = map(float, input().split())

if (B-C) < A < (B+C) and (A-C) < B < (A+C) and (A-B) < C < (A+B):
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
    
else:
    area = ((A+B)*C)/2
    print(f"Area = {area:.1f}")