from Element import Element

class List:
    def __init__(self) -> None:
        '''Construtor de uma lista'''
        self.__firstElement = None
        self.__size = 0


    def __repr__(self) -> str:
        '''Representação de uma lista'''
        string = ''
        if (self.__getFirstElement()):
            return self.__representation(self.size(), self.__getFirstElement(), string)
        else:
            return string


    def __representation(self, length, element, string) -> str:
        '''Recursividade usada para montar a representação de uma lista'''
        if (length == 1):
            string += str(element.getElement())
            return string

        length -= 1
        string += str(element.getElement()) + ' => '
        nextElement = element.getNextElement()
        return self.representation(length, nextElement, string)


    def clear(self) -> None:
        '''Limpa uma lista'''
        self.__setFirstElement(None)
        self.__setSize(0)


    def __getFirstElement(self) -> any:
        '''Retorna o primeiro elemento da lista \r\nou False caso a lista esteja vazia'''
        if (self.__firstElement == None):
            return False
        return self.__firstElement


    def __setFirstElement(self, element) -> None:
        '''Insere um elemento na primeira posição'''
        self.__firstElement = element


    def size(self) -> int:
        '''Retorna a quantidade de elementos da lista'''
        return self.__size


    def __setSize(self, quantity) -> None:
        '''Insere a quantidade de elementos na lista'''
        self.__size = quantity


    def __increaseSize(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__size += 1


    def __decreaseSize(self) -> None:
        '''Incrementa a quantidade de elementos da lista'''
        self.__size -= 1


    def insert(self, dataOfElement, position) -> bool:
        '''Insere um elemento na posição desejada\r\nRetorna True em caso de sucesso\r\nou False em caso de erro'''
        if (position < 1 or position > self.size()+1):
            return False

        element = Element(dataOfElement, None)

        if (position == 1):
            element.setNextElement(self.__getFirstElement())
            self.__setFirstElement(element)

        if (position > 1 and position <= self.size()+1):
            position -= 1
            previousElement = self.getElement(position)
            nextElement = self.getElement(position).getNextElement()
            element.setNextElement(nextElement)
            previousElement.setNextElement(element)

        self.__increaseSize()
        return True


    def remove(self, position) -> bool:
        '''Remove um elemento na posição desejada\r\nRetorna True em caso de sucesso\r\nou False em caso de erro'''
        if (position < 1 or position > self.size()):
            return False

        if (position == 1):
            self.__setFirstElement(self.__getFirstElement().getNextElement())

        if (position > 1 and position <= self.size()):
            previousElement = self.getElement(position-1)
            nextElement = self.getElement(position).getNextElement()
            previousElement.setNextElement(nextElement)

        self.__decreaseSize()
        return True


    def __searchElement(self, position, element) -> str:
        '''Recursividade usada para encontrar o elemento na posição desejada'''
        if (position == 1):
            return element.getNextElement()

        proximoElemento = element.getNextElement()
        position -= 1
        return self.__searchElement(position, proximoElemento)


    def getElement(self, position) -> any:
        '''Retorna o elemento na posição desejada\r\nou False caso não haja a posição na lista'''
        if (position < 1 or position > self.size()):
            return False

        if (position == 1):
            return self.__getFirstElement()

        return self.__searchElement(position-1, self.__getFirstElement())


    def __searchPosition(self, desiredElement, element, position, positionsFound) -> int:
        '''Recursividade usada para encontrar a posição de um elemento'''
        if (position > self.size()):
            return positionsFound

        if (desiredElement == element.getElement()):
            positionsFound.append(position)

        nextElement = element.getNextElement()
        position += 1
        return self.__searchPosition(desiredElement, nextElement, position, positionsFound)


    def getPosition(self, element) -> any:
        '''Retorna um array com a posição do elemento desejado\r\nou False caso o elemento não faça parte da lista'''
        if (self.__searchPosition(element, self.__getFirstElement(), 1, []) == []):
            return False

        return self.__searchPosition(element, self.__getFirstElement(), 1, [])
