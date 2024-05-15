salario=float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    salarionv=salario+(10/100)*salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(salario, salarionv))
else:
    salarionv=salario+(15/100)*salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(salario, salarionv))