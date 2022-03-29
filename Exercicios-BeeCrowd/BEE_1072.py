n = int(input())

x = []
for i in range(n):
    x.append(int(input()))
    
dentro = [num for num in x if num >= 10 and num <= 20]
fora = [num for num in x if num < 10 or num > 20]

print(f"{len(dentro)} in")
print(f"{len(fora)} out")        