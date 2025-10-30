#Docstring: Explicação das funcionalidades catalogadas pelo usuário na ajuda interativa do Python
def contador(i, f, p):
    """"
    -> Faz contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Isaac Tavares
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)