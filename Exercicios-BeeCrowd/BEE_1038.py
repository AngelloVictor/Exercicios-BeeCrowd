item, qtde = map(float, input().split())

precos = [4.00, 4.50, 5.00, 2.00, 1.50]

print('Total: R$ {:.2f}'.format(qtde * precos[int(item) - 1]))