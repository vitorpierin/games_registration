def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x<min) or (x>max)):
        x = int(input(pergunta))
    return x
#PROGRAMA PRINCIPAL
print('-'*10 + '-'*4 + '-'*10)
print('-'*9 + ' Menu ' + '-'*9)
print('-'*10 + '-'*4 + '-'*10)
print('Opção 1 - Novo Item')
print('Opção 2 - Listar Itens')
print('Opção 3 - Sair')

op = valida_int('Escolha a opção desejada: ', 1, 3)
