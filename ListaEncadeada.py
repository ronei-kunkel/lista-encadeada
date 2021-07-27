from Elemento import Elemento

class Lista:
    def __init__(self) -> None:
        '''Construtor de uma lista'''
        self.__primeiro = None
        self.__quantidade = 0

    def __repr__(self) -> str:
        '''Representação de uma lista'''
        string = '['
        if (self.getPrimeiroElemento()):
            return self.recursaoRepresentacao(self.getQuantidadeElementos(), self.getPrimeiroElemento(), string) + ']'
        else:
            return string + ']'

    def recursaoRepresentacao(self, tamanho, elemento, string) -> str:
        '''Recursividade usada para montar a representação de uma lista'''
        if (tamanho == 1):
            string += str(elemento.getDado())
            return string

        tamanho -= 1
        string += str(elemento.getDado()) + ', '
        proximoElemento = elemento.getProximo()
        return self.recursaoRepresentacao(tamanho, proximoElemento, string)

    def clearLista(self) -> None:
        '''Limpa uma lista'''
        self.setPrimeiroElemento(None)
        self.setQuantidadeElementos(0)

    def getPrimeiroElemento(self) -> any:
        '''Retorna o primeiro elemento da lista 

        ou False caso a lista esteja vazia'''
        if (self.__primeiro == None):
            return False
        return self.__primeiro

    def setPrimeiroElemento(self, elemento) -> None:
        '''Insere um elemento na primeira posição'''
        self.__primeiro = elemento

    def getQuantidadeElementos(self) -> int:
        '''Retorna a quantidade de elementos da lista'''
        return self.__quantidade

    def setQuantidadeElementos(self, quantidade) -> None:
        '''Insere a quantidade de elementos na lista'''
        self.__quantidade = quantidade

    def incrementaQuantidadeElementos(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__quantidade += 1
    
    def decrementaQuantidadeElementos(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__quantidade -= 1

    def insertElementoNaPosicao(self, dado, posicao) -> bool:
        '''Insere um elemento na posição desejada

        Retorna True em caso de sucesso
        ou False em caso de erro'''
        if (posicao < 1 or posicao > self.getQuantidadeElementos()+1):
            return False

        elemento = Elemento(dado, None)

        if (posicao == 1):
            elemento.setProximo(self.getPrimeiroElemento())
            self.setPrimeiroElemento(elemento)

        if (posicao > 1 and posicao <= self.getQuantidadeElementos()+1):
            posicao -= 1
            elementoAnterior = self.getElementoNaPosicao(posicao)
            proximoElemento = self.getElementoNaPosicao(posicao).getProximo()
            elemento.setProximo(proximoElemento)
            elementoAnterior.setProximo(elemento)

        self.incrementaQuantidadeElementos()
        return True

    def removeElementoNaPosicao(self, posicao) -> bool:
        '''Remove um elemento na posição desejada

        Retorna True em caso de sucesso
        ou False em caso de erro'''
        if (posicao < 1 or posicao > self.getQuantidadeElementos()):
            return False

        if (posicao == 1):
            self.setPrimeiroElemento(self.getPrimeiroElemento().getProximo())

        if (posicao > 1 and posicao <= self.getQuantidadeElementos()):
            elementoAnterior = self.getElementoNaPosicao(posicao-1)
            proximoElemento = self.getElementoNaPosicao(posicao).getProximo()
            elementoAnterior.setProximo(proximoElemento)

        self.decrementaQuantidadeElementos()
        return True

    def recursaoGetElementoNaPosicao(self, posicao, elemento) -> str:
        '''Recursividade usada para encontrar o elemento na posição desejada'''
        if (posicao == 1):
            return elemento.getProximo()

        proximoElemento = elemento.getProximo()
        posicao -= 1
        return self.recursaoGetElementoNaPosicao(posicao, proximoElemento)

    def getElementoNaPosicao(self, posicao) -> any:
        '''Retorna o elemento na posição desejada

        ou False caso não haja a posição na lista'''
        if (posicao < 1 or posicao > self.getQuantidadeElementos()):
            return False

        if (posicao == 1):
            return self.getPrimeiroElemento()

        return self.recursaoGetElementoNaPosicao(posicao-1, self.getPrimeiroElemento())

    def recursaoGetPosicaoDoElemento(self, elementoDesejado, elemento, posicao, arrayDePosicoes) -> int:
        '''Recursividade usada para encontrar a posição de um elemento'''
        if (posicao > self.getQuantidadeElementos()):
            return arrayDePosicoes

        if (elementoDesejado == elemento.getDado()):
            arrayDePosicoes.append(posicao)

        proximoElemento = elemento.getProximo()
        posicao += 1
        return self.recursaoGetPosicaoDoElemento(elementoDesejado, proximoElemento, posicao, arrayDePosicoes)

    def getPosicaoDoElemento(self, elemento) -> any:
        '''Retorna um array com a posição do elemento desejado

        ou False caso o elemento não faça parte da lista'''
        if (self.recursaoGetPosicaoDoElemento(elemento, self.getPrimeiroElemento(), 1, []) == []):
            return False
        
        return self.recursaoGetPosicaoDoElemento(elemento, self.getPrimeiroElemento(), 1, [])
