class Comanda(object):

    def __init__(self, valor=None, codigo=None, bebida=None, alimento=None,
                 quantidade_bebida=None, quantidade_alimento=None):
        self.__valor = valor
        self.__codigo = codigo
        self.__bebida = bebida
        self.__alimento = alimento
        self.__quantidade_bebida = quantidade_bebida
        self.__quantidade_alimento = quantidade_alimento

        # Index do iterador
        self.index = 0

        # Campos do iterador
        self.items = ["_Comanda__codigo",
                      "_Comanda__quantidade_bebida",
                      "_Comanda__bebida",
                      "_Comanda__quantidade_alimento",
                      "_Comanda__alimento",
                      "_Comanda__valor"]


    def __del__(self):
        print 'RIP Comanda'

    # Iterador == 0
    def __iter__(self):
        return self

    # Iterador += 1
    def next(self):
        if self.index < len(self.items):
            self.index += 1
            k = self.items[self.index - 1]
            return (k.replace('_Comanda__', ''), getattr(self, k))
        else:
            # zera o iterador
            self.index = 0
            raise StopIteration

    #Sobrecarga toString
    def __str__(self):
        return str(self.__dict__).replace('_Comanda__', '')

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def draw(self):
        f = open('./GUI/comandas.tpl', 'a')
        for atribute, value in self:
            if not value:
                value = None
            f.write('<p>' + str(atribute.upper()) + ' : <b>' + str(value) + '</b></p>' + '\n')
        f.write('<p>------------------------------------------------</p>\n')
        f.close()

    def getCodigo(self):
        return self.__codigo

    def getQuantidadeBebida(self):
        return self.__quantidade_bebida

    def getBebida(self):
        return self.__bebida

    def getQuantidadeAlimento(self):
        return self.__quantidade_alimento

    def getValor(self):
        return self.__valor

    def setCodigo(self, codigo):
        self.__codigo = codigo
        return True

    def setQuantidadeBebida(self, quantidade_bebida):
        self.__quantidade_bebida = quantidade_bebida
        return True

    def setBebida(self, bebida):
        self.__bebida = bebida
        return True

    def setQuantidadeAlimento(self, quantidade_alimento):
        self.__quantidade_alimento = quantidade_alimento
        return True

    def setAlimento(self, alimento):
        self.__alimento = alimento
        return True

    def getAlimento(self):
        return self.__alimento

    def setValor(self, valor):
        self.__valor = valor
        return True
