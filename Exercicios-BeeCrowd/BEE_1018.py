
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    novo_notas = (valor // nota)
    valor = valor - novo_notas * nota
    print(f"{novo_notas} nota(s) de R$ {nota},00")



