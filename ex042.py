l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Teerceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    #", end=''" significa que o texto da próxima linha não será dado parágrafo. Continuará na mesma linha
    if l1 == l2 == l3:
        #poderia ser 'l1 == l2 and l2 == l3'
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        #Nesse caso, l3 tem q ser diferente tb de l1, senão o isósceles tb poderia dar escaleno.
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')