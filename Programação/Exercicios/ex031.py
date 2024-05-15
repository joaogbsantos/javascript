distancia=float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a fazer uma viagem de {:.1f}Km. '.format(distancia))

if distancia < 200:
    valor=distancia*0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
else:
    valor=distancia*0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))

