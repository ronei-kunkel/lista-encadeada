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
    def __init__(self, elemento) -> None:
        '''Construtor de lista
        
        Recebe o elemento que encabeça a lista'''
        self.__primeiro = elemento
    
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
