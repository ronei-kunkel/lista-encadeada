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
    def __init__(self, elemento):
        '''Construtor de lista'''
        self.__elemento = elemento
        self.__head = None
    
    def __repr__(self):
        '''Representação de lista'''
        return '['+']'
