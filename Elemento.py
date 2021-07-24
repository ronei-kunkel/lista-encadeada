class Elemento:
    def __init__(self, dado, proximo) -> None:
        '''Construtor de um elemento'''
        self.__dado = dado
        self.__proximo = proximo

    def __repr__(self) -> str:
        '''Representação de um elemento'''
        string = ''
        if (self.getProximoElemento()):
            string += str(self.getElemento()) + ' ➞ ' + str(self.getProximoElemento())
            return string
        else:
            return string + str(self.getElemento())

    def getElemento(self) -> object:
        '''Retorna o dado de um elemento'''
        return self.__dado

    def getProximoElemento(self) -> any:
        '''Retorna o elemento seguinte ao atual ou False caso não houver'''
        if (self.__proximo == None):
            return False
        return self.__proximo

    def setProximo(self, proximo) -> None:
        '''Define qual o próximo elemento do atual'''
        self.__proximo = proximo