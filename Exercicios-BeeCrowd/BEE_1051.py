salario = float(input())


if salario > 0 and salario <= 2000:
    print('Isento')
    
elif salario > 2000 and salario <= 3000:
    sobra =     salario - 2000
    print('R$ {:.2f}'.format( (sobra * 0.08)))
    
elif salario > 3000 and salario <= 4500:
    sobra = salario - 3000
    print('R$ {:.2f}'.format((sobra * 0.18) + (1000 * 0.08)))
    
elif salario > 4500:
    sobra = salario - 4500
    print('R$ {:.2f}'.format((sobra * 0.28) + (1500 * 0.18) + (1000 * 0.08)))