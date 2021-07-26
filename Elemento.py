class Elemento:
    def __init__(self, dado, elemento) -> None:
        '''Construtor de um elemento

        Recebe um valor para o elemento e outro elemento para qual ele aponta'''
        self.__dado = dado
        self.__proximo = elemento

    def __repr__(self) -> str:
        '''Representação de um elemento'''
        return str(self.getDado())

    def getDado(self) -> object:
        '''Retorna o dado de um elemento'''
        return self.__dado

    def getProximo(self) -> any:
        '''Retorna o elemento seguinte ao atual 

        ou False caso não houver'''
        if (self.__proximo == None):
            return False
        return self.__proximo

    def setProximo(self, elemento) -> None:
        '''Define qual o próximo elemento do atual'''
        self.__proximo = elemento
