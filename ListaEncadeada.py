from Elemento import Elemento

#-------------------------------------------------------#
#   Checklist:                                          #
#  ok   Inserir na posição | Valor - Posição            #
#       Remover da posição                              #
#  ok   Procurar o valor de acordo com a posição        #
#       Procurar a posição de acordo com o valor        #
#  ok   Destruir a lista                                #
#-------------------------------------------------------#

class Lista:
    def __init__(self) -> None:
        '''Construtor de lista'''
        self.__primeiro = None
        self.__quantidade = 0

    def __repr__(self) -> str:
        '''Representação de lista'''
        string = '['
        if (self.getPrimeiro()):
            return self.recursaoRepresentacao(self.getQuantidadeElementos(), self.getPrimeiro(), string) + ']'
        else:
            return string + ']'

    def recursaoRepresentacao(self, tamanho, elemento, string):
        if (tamanho == 1):
            string += elemento.getDado()
            return string
        
        tamanho -= 1
        string += elemento.getDado() + ', '
        proximoElemento = elemento.getProximoElemento()
        return self.recursaoRepresentacao(tamanho, proximoElemento, string)

    def clearLista(self) -> None:
        '''Limpa a lista'''
        self.setPrimeiro(None)
        self.setQuantidadeElementos(0)

    def getPrimeiro(self) -> any:
        '''Retorna o primeiro elemento da lista 

        ou False caso a lista esteja vazia'''
        if (self.__primeiro == None):
            return False
        return self.__primeiro

    def setPrimeiro(self, elemento) -> None:
        '''Insere um elemento na primeira posição'''
        self.__primeiro = elemento

    def incrementaQuantidadeElementos(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__quantidade += 1

    def insertElementoNaPosicao(self, dado, posicao) -> bool:
        '''Insere um elemento na posição desejada

        Retorna True em caso de sucesso
        ou False em caso de erro'''
        if (posicao < 1 or posicao > self.getQuantidadeElementos()+1):
            return False

        elemento = Elemento(dado, None)

        if (posicao == 1):
            elemento.setProximo(self.getPrimeiro())
            self.setPrimeiro(elemento)

        if (posicao > 1 and posicao <= self.getQuantidadeElementos()+1):
            elementoAnterior = self.getElementoNaPosicao(posicao-1)
            proximoElemento = self.getElementoNaPosicao(posicao-1).getProximoElemento()
            elemento.setProximo(proximoElemento)
            elementoAnterior.setProximo(elemento)

        self.incrementaQuantidadeElementos()
        return True

    def getQuantidadeElementos(self) -> int:
        '''Retorna a quantidade de elementos da lista'''
        return self.__quantidade

    def setQuantidadeElementos(self, quantidade) -> None:
        '''Insere a quantidade de elementos na lista'''
        self.__quantidade = quantidade

    def recursaoGetElementoNaPosicao(self, posicao, elemento) -> str:
        '''Recursividade usada para encontrar o elemento na posição desejada'''
        if (posicao == 1):
            return elemento.getProximoElemento()

        proximoElemento = elemento.getProximoElemento()
        posicao -= 1
        return self.recursaoGetElementoNaPosicao(posicao, proximoElemento)

    def getElementoNaPosicao(self, posicao) -> any:
        '''Retorna o elemento na posição desejada

        ou False caso não haja a posição na lista'''
        if (posicao < 1 or posicao > self.getQuantidadeElementos()):
            return False

        if (posicao == 1):
            return self.getPrimeiro()

        return self.recursaoGetElementoNaPosicao(posicao-1, self.getPrimeiro())
