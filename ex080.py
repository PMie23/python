valores = []
cont = 0
for v in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if v == 0:                                      # Se o número for o primeiro valor,
        valores.append(n)                           # Será add como primeiro valor
        print('Adicionado ao final da lista.')
    elif n > valores[-1]:                           # Se o número for > que o ultimo núm da lista
        valores.append(n)                           # Adiciona no fim da lista
    else:
        pos = 0
        while pos < len(valores):                   # Se não, loop para o 'pos' do 0 ate a ultima posição
            if n <= valores[pos]:                   # Se o valor for menor ou igual a posição que ele esta
                valores.insert(pos, n)              # Insere ele na posição que ficou menor
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
