valor =float(input())
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]


print("NOTAS:")
for nota in notas:
    novo_notas = (valor // nota)
    valor = valor - novo_notas * nota
    print(f"{novo_notas} nota(s) de R$ {nota}")
    
    
print("MOEDAS:")    
for moeda in moedas:
    novo_moedas = (valor // moeda)
    valor = valor - novo_moedas * moeda
    print(f"{novo_moedas} moedas(s) de R$ {moeda}")