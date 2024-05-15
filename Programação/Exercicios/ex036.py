valor_casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos_financiamento = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa/(anos_financiamento*12)
limite_crédito = 0.3*salario

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.'.format(valor_casa, anos_financiamento, prestacao))
if prestacao < limite_crédito:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')