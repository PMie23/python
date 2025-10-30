def newLine(msg):           # "def" define uma função que será configurada pelo usuário
    print('-=' * 10)        # "newLine é o nome qualquer colocado para a função
    print(msg)              # "msg" é a msg (parâmetro) que poderá ser criada/modificada toda vez q a função for usada
    print('-=' * 10)        # os prints de baixo são o conteúdo da função; o que irá aer feito qnd usar a função

                            # pular sempre 2 linhas depois da função como "boas práticas"
newLine('   Boas Vindas!!   ')    # chamou a função nova e colocou a primeira "msg" (parâmetro)
newLine('   Essa é Cork!!   ')    # segunda utilização da função com novo parâmetro
print(newLine)