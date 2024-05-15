from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade >= 20 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')