from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18: 
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18 :
    saldo = idade - 18
    print('Você já devieria ter se alistado há {} anos.'.format(saldo))