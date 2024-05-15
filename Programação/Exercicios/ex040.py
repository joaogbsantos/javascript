nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2

print('Tirando {:.1f} e {:.1f}, a média doo aluno é {}'.format(nota1, nota2, media))

if media >= 7.0:
    print('O aluno está APROVADO.')
elif media >= 5.0 and media < 7.0:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')