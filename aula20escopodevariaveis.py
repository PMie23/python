def teste():                                    {
    x = 8                                       {Escopo
    print(f'Na função teste, n vale {n}.')      {Local
    print(f'Na função teste, x vale {x}.')      {

#Programa Principal                             {
n = 2                                           {Escopo
print(f'No programa principal, n vale {n}.')    {Global
teste()                                         {

# Este programa dá erro pq a variável "x" so existe no escopo local