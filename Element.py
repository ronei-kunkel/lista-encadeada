class Element:
    def __init__(self, dataOfElement, nextElement) -> None:
        '''Construtor de um elemento \r\nRecebe um valor para o elemento e outro elemento para qual ele aponta'''
        self.__element = dataOfElement
        self.__nextElement = nextElement

    def __repr__(self) -> str:
        '''Representação de um elemento'''
        return str(self.getElement())

    def getElement(self) -> any:
        '''Retorna o dado de um elemento'''
        return self.__element

    def getNextElement(self) -> any:
        '''Retorna o elemento seguinte ao atual \r\nou False caso não houver'''
        if (self.__nextElement == None):
            return False
        return self.__nextElement

    def setNextElement(self, nextElement) -> None:
        '''Define qual o próximo elemento do atual'''
        self.__nextElement = nextElement
