class Cliente(object):

    def __init__(self, nome=None, cpf=None, idade=None, email=None, telefone=None, cidade=None, pais=None,
                 rua=None, bairro=None, numero=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__email = email
        self.__telefone = telefone
        self.__cidade = cidade
        self.__pais = pais
        self.__rua = rua
        self.__bairro = bairro
        self.__numero = numero
        # Index do iterador
        self.index = 0

        # Campos do iterador
        self.items = ["_Cliente__nome",
                      "_Cliente__cpf",
                      "_Cliente__idade",
                      "_Cliente__email",
                      "_Cliente__telefone",
                      "_Cliente__cidade",
                      "_Cliente__pais",
                      "_Cliente__rua",
                      "_Cliente__bairro",
                      "_Cliente__numero"]

    def __del__(self):
        print 'RIP Cliente'

    # Iterador == 0
    def __iter__(self):
        return self

    # Iterador += 1
    def next(self):
        if self.index < len(self.items):
            self.index += 1
            k = self.items[self.index - 1]
            return (k.replace('_Cliente__', ''), getattr(self, k))
        else:
            # zera o iterador
            self.index = 0
            raise StopIteration

    #Sobrecarga toString
    def __str__(self):
        return str(self.__dict__).replace('_Cliente__', '')

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def draw(self):
        f = open('.\GUI\clientes.tpl', 'a')
        for atribute, value in self:
            if not value:
                value = None
            f.write('<p>' + str(atribute.upper()) + ' : <b>' + str(value) + '</b></p>' + '\n')
        f.write('<p>------------------------------------------------</p>\n')
        f.close()

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
        return True

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone
        return True

    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        self.__cidade = cidade
        return True

    def getPais(self):
        return self.__pais

    def setPais(self, pais):
        self.__pais = pais
        return True

    def getRua(self):
        return self.__rua

    def setRua(self, rua):
        self.__rua = rua
        return True

    def getBairro(self):
        return self.__bairro

    def setBairro(self, bairro):
        self.__bairro = bairro
        return True

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero
        return True

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
        return True

    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpf):
        self.__cpf = cpf
        return True

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade
        return True
