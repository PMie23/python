n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Sua média entre {} e {} é igual a {}.'.format(n1, n2, media))
if media < 5:
    print('O aluno está REPROVADO!')
elif 6.9 >= media >= 5:
    #media >= 5 and media <= 6.9 (Essa seria a forma mais básica para a estrutura acima)
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7:
    #Ou 'else:'
    print('O aluno está APROVADO!')