from List import List
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu(return_ = None, list_ = None):
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
    print('|                  LISTA                   |')
    print('+------------------------------------------+')
    print()
    if not 'list_' in globals() or list_ == None:
        print('Sem lista')
    else:
        print('Lista vazia' if list_ == [] else list_)
    print()
    if return_:
        print('+-----------------RETORNO------------------+')
        print()
        print(return_+'\n')
    print('+-------------------AÇÃO-------------------+')

exec = True
menu()

while exec:
    if not 'list_' in globals() or not 'list_' in locals():
        list_ = None

    option = input('Selecione uma opção: ')

    while not option.isnumeric():
        menu(f'Opção {option} inválida!', list_)
        option = input('Selecione uma opção: ')
    
    if option.isnumeric():
        option = int(option)

    if option < 0 or option > 8 :
        menu(f'Não existe a opção de número {option}!', list_)

    if option == 0:
        print('SAINDO...')
        exec = False
    
    if option == 1:
        if list_ != None:
            menu('Sua lista já existe e não é possível criar mais de uma!', list_)
            continue
        list_ = List()
        menu('Sua lista foi criada!', list_)

    if option == 2:
        if list_ == None:
            menu('Não é possível deletar uma lista que não existe!', list_)
            continue
        list_.clear()
        del list_
        menu('Sua lista foi eliminada!', None)

    if option == 3:
        if list_ == None:
            menu('Você não pode inserir elementos em uma lista que não existe!', list_)
            continue

        selection = ''
        while selection not in ['i', 'I', 'c', 'C']:
            if selection != '':
                menu('Opção inválida!', list_)
            selection = input('Você deseja inserir um elemento numérico inteiro(I) ou um elemento caractere(C)? (I,C): ')

        if selection in ['i', 'I']:
            element = int(input('\nInsira um elemento numérico inteiro: '))
        
        if selection in ['c', 'C']:
            element = input('\nInsira um elemento caractere: ')
        
        position = int(input(f'\nEm qual posição você quer inserir o elemento *{element}*?\nPosições disponíveis de 1 até {list_.size()+1}: '))

        if list_.insert(element, position):
            menu(f'Elemento {element} adicionado na posição {position}', list_)
            continue
        menu(f'Não foi possível inserir um elemento na posição {position}', list_)

    if option == 4:
        if list_ == None:
            menu('Você não pode remover elementos de uma lista que não existe!', list_)
            continue

        if list_.size() == 0:
            menu('Você não pode remover elementos de uma lista que não possui elementos!', list_)
            continue

        number = list_.size()
        arrayOfNumberOfElements = []

        while number > 0:
            arrayOfNumberOfElements.append(int(number))
            number -= number

        position = '@!?|pop'
        while position not in arrayOfNumberOfElements:
            if position != '@!?|pop':
                menu('Opção inválida!', list_)
            position = input(f'Você quer remover o elemento de qual posição?\nPosições disponíveis de 1 até {list_.size()}: ')
            if position.isnumeric():
                position = int(position)

        if list_.getElement(position):
            element = list_.getElement(position)

        if list_.remove(position):
            menu(f'Elemento *{element}* removido da posição *{position}*', list_)
            continue

        menu(f'Não foi possível remover o elemento *{element}* da posição *{position}*', list_)

    if option == 5:
        if list_ == None:
            menu('Não há posições em uma lista que não existe!', list_)
            continue

        if list_.size() == 0:
            menu('Não há nenhum elemento para ser encontrado!', list_)
            continue

        selection = ''

        while selection not in ['i', 'I', 'c', 'C']:
            if selection != '':
                menu('Opção inválida!', list_)
            selection = input('Você deseja encontrar a posição de um elemento numérico inteiro[I] ou um elemento caractere[C]? [I,C]: ')

        if selection in ['i', 'I']:
            element = int(input('\nInsira um elemento numérico inteiro: '))
        
        if selection in ['c', 'C']:
            element = input('\nInsira um elemento caractere: ')
        
        if list_.getPosition(element):
            elementos = list_.getPosition(element)
            return_ = f'seu elemento *{element}* se encontra na(s) posição(ões): '
            for element in elementos:
                if element == elementos[-1]:
                    return_ += str(element)
                else:
                    return_ += str(element) + ' e '
            menu(return_, list_)
            continue

        menu(f'Não foi possível encontrar o elemento *{element}*', list_)

    if option == 6:
        if list_ == None:
            menu('Não existem elementos para procurar em uma lista que não exite!', list_)
            continue

        if list_.size() == 0:
            menu('Não há nenhum elemento para ser encontrado!', list_)
            continue

        position = int(input('Você deseja procurar um elemento em qual posição?'))

        if not list_.getElement(position):
            menu(f'Não foi possível encontrar nenhum elemento na posição *{position}*', list_)
            continue
        menu(f'O elemento da posição *{position}* é: *{list_.getElement(position)}*', list_)

    if option == 7:
        if list_ == None:
            menu('Você não pode exibir uma lista que você não criou ainda!', list_)
            continue
        menu('A lista é sempre exibida acima', list_)

    if option == 8:
        if (list_ == None):
            menu('Lista que não existe não tem tamanho!', list_)
            continue

        if list_.size() == 0:
            menu('Não há nenhum elemento na lista!', list_)
            continue

        menu(f'Quantidade de elementos na lista: {list_.size()}', list_)
