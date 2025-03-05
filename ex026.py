frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
# Foi colocado o "+1" para que fique como a gente conta normalmente: 1ª posição, posição 1.
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))