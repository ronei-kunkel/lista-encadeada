from ListaEncadeada import Lista
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    clear()
    print('+------------------------------------------+')
    print('|                  OPÇÕES                  |')
    print('+------------------------------------------+')
    print('| 1 - Criar uma lista vazia                |')
    print('| 2 - Deletar a lista                      |')
    print('| 3 - Adicionar elementos em uma posição   |')
    print('| 4 - Remover elemento em uma posição      |')
    print('| 5 - Encontrar a posição de um elemento   |')
    print('| 6 - Encontrar um elemento em uma posição |')
    print('| 7 - Exibir a lista                       |')
    print('| 8 - Exibir a quantidade de elementos     |')
    print('| 0 - SAIR                                 |')
    print('+------------------------------------------+')
    print('+-----------------RETORNO------------------+')

exec = True
lista = None
menu()

while exec:
    opcao = input('Selecione uma opção: ')

    while not opcao.isnumeric():
        menu()
        print(f'Opção {opcao} inválida!')
        opcao = input('Selecione uma opção: ')
    
    if opcao.isnumeric():
        opcao = int(opcao)

    if (opcao < 0 or opcao > 7 ):
        menu()
        print(f'Não existe a opção de número {opcao}!')

    if opcao == 0:
        print('SAINDO...')
        exec = False
    
    if opcao == 1:
        if (lista != None):
            menu()
            print('Sua lista já existe e não é possível criar mais de uma!\n')
            continue
        menu()
        lista = Lista()
        print('Sua lista foi criada!\n')

    if opcao == 2:
        if (lista == None):
            menu()
            print('Sua lista não existe!\nNão é possível deletar algo que não existe!\n')
            continue
        menu()
        lista.clearLista()
        lista = None
        print('Sua lista foi elminada!\n')
    
    if opcao == 3:

        if (lista == None):
            menu()
            print('Você não pode inserir elementos em uma lista que não existe!\n')
            continue
        
        selecao = input('Você deseja inserir um elemento numérico inteiro[I] ou um elemento caractere[C]? [I,C]: ')
        
        if (selecao == 'i' or selecao == 'I'):
            elemento = int(input('\nInsira um elemento numérico inteiro: '))
        
        if (selecao == 'c' or selecao == 'C'):
            elemento = input('\nInsira um elemento caractere: ')
        
        posicao = int(input(f'\nEm qual posição você quer inserir o elemento *{elemento}*?\nPosições disponíveis de 1 até {lista.getQuantidadeElementos()+1}: '))

        menu()
        
        if (lista.insertElementoNaPosicao(elemento, posicao)):
            print(f'Elemento {elemento} adicionado na posição {posicao}')
            print(f'Sua lista:\n{lista}\n')
            continue
        print(f'Não foi possível inserir um elemento na posição {posicao}')

    if opcao == 4:
        if (lista == None):
            menu()
            print('Você não pode remover elementos de uma lista que não existe!\n')
            continue
        
        print(f'Sua lista:\n{lista}\n')
        
        posicao = int(input(f'Você quer remover o elemento de qual posição?\nPosições disponíveis de 1 até {lista.getQuantidadeElementos()}: '))

        if (lista.getElementoNaPosicao(posicao)):
            elemento = lista.getElementoNaPosicao(posicao)

        menu()

        if (lista.removeElementoNaPosicao(posicao)):
            print(f'Elemento *{elemento}* removido com sucesso da posição *{posicao}*')
            print(f'Sua lista:\n{lista}\n')
            continue

        print(f'Não foi possível remover o elemento da posição *{posicao}*')

    if opcao == 5:

        if (lista == None):
            menu()
            print('Sua lista está vazia!\nNão há elementos para procurar!\n')
            continue


        print(f'Sua lista:\n{lista}\n')

        selecao = input('Você deseja encontrar a posição de um elemento numérico inteiro[I] ou um elemento caractere[C]? [I,C]: ')

        if (selecao == 'i' or selecao == 'I'):
            elemento = int(input('\nInsira um elemento numérico inteiro: '))
        
        if (selecao == 'c' or selecao == 'C'):
            elemento = input('\nInsira um elemento caractere: ')
        
        if (lista.getPosicaoDoElemento(elemento)):
            menu()
            elementos = lista.getPosicaoDoElemento(elemento)
            string = f'seu elemento *{elemento}* se encontra na(s) posição(ões): '
            for elemento in elementos:
                if (elemento == elementos[-1]):
                    string += str(elemento)
                else:
                    string += str(elemento) + ' e '
            print(string)
            continue

        menu()
        print(f'Não foi possível encontrar o elemento *{elemento}*')

    if opcao == 6:
        
        if (lista == None):
            menu()
            print('Sua lista está vazia!\nNão há elementos para procurar!\n')
            continue

        print(f'Sua lista:\n{lista}\n')

        posicao = int(input('Você deseja procurar um elemento em qual posição?'))

        if (lista.getElementoNaPosicao(posicao)):
            menu()
            print(f'O elemento da posição *{posicao}* é: *{lista.getElementoNaPosicao(posicao)}*')
            continue

        menu()
        print(f'Não foi possível encontrar nenhum elemento na posição *{posicao}*')

    if opcao == 7:

        if (lista == None):
            menu()
            print('Você não pode exibir uma lista que você não criou ainda!\n')
        menu()
        print(f'Sua lista:\n{lista}\n')

    if opcao == 8:

        if (lista == None):
            menu()
            print('Lista que não existe não tem tamanho!\n')

        menu()
        print(f'Quantidade de elementos na lista: {lista.getQuantidadeElementos()}')
