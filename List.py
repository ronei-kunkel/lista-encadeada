from Element import Element

class List:
    def __init__(self) -> None:
        '''Construtor de uma lista'''
        self.__firstElement = None
        self.__numberOfElements = 0


    def __repr__(self) -> str:
        '''Representação de uma lista'''
        string = '['
        if (self.getFirstElement()):
            return self.representation(self.getNumberOfElements(), self.getFirstElement(), string) + ']'
        else:
            return string + ']'


    def representation(self, length, element, string) -> str:
        '''Recursividade usada para montar a representação de uma lista'''
        if (length == 1):
            string += str(element.getElement())
            return string

        length -= 1
        string += str(element.getElement()) + ', '
        nextElement = element.getNextElement()
        return self.representation(length, nextElement, string)


    def clear(self) -> None:
        '''Limpa uma lista'''
        self.setFirstElement(None)
        self.setNumberOfElements(0)


    def getFirstElement(self) -> any:
        '''Retorna o primeiro elemento da lista 

        ou False caso a lista esteja vazia'''
        if (self.__firstElement == None):
            return False
        return self.__firstElement


    def setFirstElement(self, element) -> None:
        '''Insere um elemento na primeira posição'''
        self.__firstElement = element


    def getNumberOfElements(self) -> int:
        '''Retorna a quantidade de elementos da lista'''
        return self.__numberOfElements


    def setNumberOfElements(self, quantity) -> None:
        '''Insere a quantidade de elementos na lista'''
        self.__numberOfElements = quantity


    def increaseNumberOfElements(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__numberOfElements += 1


    def decreaseNumberOfElements(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__numberOfElements -= 1


    def insert(self, dataOfElement, position) -> bool:
        '''Insere um elemento na posição desejada

        Retorna True em caso de sucesso
        ou False em caso de erro'''
        if (position < 1 or position > self.getNumberOfElements()+1):
            return False

        element = Element(dataOfElement, None)

        if (position == 1):
            element.setNextElement(self.getFirstElement())
            self.setFirstElement(element)

        if (position > 1 and position <= self.getNumberOfElements()+1):
            position -= 1
            previousElement = self.getElement(position)
            nextElement = self.getElement(position).getNextElement()
            element.setNextElement(nextElement)
            previousElement.setNextElement(element)

        self.increaseNumberOfElements()
        return True


    def remove(self, position) -> bool:
        '''Remove um elemento na posição desejada

        Retorna True em caso de sucesso
        ou False em caso de erro'''
        if (position < 1 or position > self.getNumberOfElements()):
            return False

        if (position == 1):
            self.setFirstElement(self.getFirstElement().getNextElement())

        if (position > 1 and position <= self.getNumberOfElements()):
            previousElement = self.getElement(position-1)
            nextElement = self.getElement(position).getNextElement()
            previousElement.setNextElement(nextElement)

        self.decreaseNumberOfElements()
        return True


    def searchElement(self, position, element) -> str:
        '''Recursividade usada para encontrar o elemento na posição desejada'''
        if (position == 1):
            return element.getNextElement()

        proximoElemento = element.getNextElement()
        position -= 1
        return self.searchElement(position, proximoElemento)


    def getElement(self, position) -> any:
        '''Retorna o elemento na posição desejada

        ou False caso não haja a posição na lista'''
        if (position < 1 or position > self.getNumberOfElements()):
            return False

        if (position == 1):
            return self.getFirstElement()

        return self.searchElement(position-1, self.getFirstElement())


    def searchPosition(self, desiredElement, element, position, positionsFound) -> int:
        '''Recursividade usada para encontrar a posição de um elemento'''
        if (position > self.getNumberOfElements()):
            return positionsFound

        if (desiredElement == element.getElement()):
            positionsFound.append(position)

        nextElement = element.getNextElement()
        position += 1
        return self.searchPosition(desiredElement, nextElement, position, positionsFound)


    def getPosition(self, element) -> any:
        '''Retorna um array com a posição do elemento desejado

        ou False caso o elemento não faça parte da lista'''
        if (self.searchPosition(element, self.getFirstElement(), 1, []) == []):
            return False

        return self.searchPosition(element, self.getFirstElement(), 1, [])
