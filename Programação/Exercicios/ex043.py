peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso/altura**2
print('O IMC desta pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está em OBESIDADE!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEIAL!')
elif imc >= 25 and imc < 30:
    print('Você está  em SOBREPESO!')
elif imc >= 30 and imc < 40: 
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA')