num = soma = cont = 0
#Esse comando de cima informa que todas as 3 variáveis começarão com 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
    #Dessa forma, o flag (que é o comando de parada) não será somado no final, não sendo necessário o "-1" e o "-999"
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
