def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x<min) or (x>max)):
        x = int(input(pergunta))
    return x

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print('Arquivo {} foi criado com sucesso! \n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideoGame))
    finally:
        a.close()
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        print(a.read())
    finally:
        a.close()

#PROGRAMA PRINCIPAL
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:
    print('-'*10 + '-'*4 + '-'*10)
    print('-'*9 + ' Menu ' + '-'*9)
    print('-'*10 + '-'*4 + '-'*10)
    print('Opção 1 - Novo Item')
    print('Opção 2 - Listar Itens')
    print('Opção 3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)

    if(op==1):
        nomeJogo = input('Nome do jogo: ')
        nomeVideoGame = input('Nome do video game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
    elif(op==2):
        listarArquivo(arquivo)
    elif(op==3):
        print('Encerrrando programa...')
        break