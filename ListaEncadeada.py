from Elemento import Elemento

#-------------------------------------------------------#
#   Checklist:                                          #
#       Inserir na posição | Valor - Posição            #
#       Remover da posição                              #
#       Procurar o valor de acordo com a posição        #
#       Procurar a posição de acordo com o valor        #
#       Destruir a lista                                #
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
            string += str(self.getPrimeiro()) + ']'
            return string.replace(' ➞ ', ', ')
        else:
            return string + ']'

    def getPrimeiro(self) -> any:
        '''Retorna o elemento que encabeça a lista 
        
        ou False caso não houver'''
        if (self.__primeiro == None):
            return False
        return self.__primeiro

    def insertElementoNaPosicao(self, dado, posicao) -> bool:
        '''Insere um elemento na posição passada'''
        elemento = Elemento(dado, None)

        if (posicao == 1):
            elemento.setProximo(self.getPrimeiro())
            self.setPrimeiro(elemento)
            return True
        if (posicao >= 2):
            return False
        
        if (posicao == self.getQuantidadeElementos(self.getPrimeiro())):
            pass

    def getQuantidadeElementos(self) -> int:

        self.recursao(self.getPrimeiro())

        return self.__quantidade

    def recursao(self, elemento) -> int:
        '''Retorna a quantidade de elementos da lista'''

        if (not elemento.getProximoElemento()):
            self.__quantidade += 1
            return self.__quantidade

        proximoElemento = elemento.getProximoElemento()
        self.__quantidade += 1
        return self.recursao(proximoElemento)



    #DEDBUGS
    def setPrimeiro(self, elemento) -> None:
        '''Insere um elemento na primeira posição'''
        self.__primeiro = elemento