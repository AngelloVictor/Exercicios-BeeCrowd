n = int(input())

for i in range(n):
    a,b,c = map(float, input().split())
    total = (a*0.2 + b*0.3 + c*0.5)
    print("{:.1f}".format(total))
          