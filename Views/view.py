class View(object):

    def __init__(self, nome=None):
        self.__nome = nome

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def draw(self, objects, clean=None):
        if clean == "clientes":
            cleanClienteView = open('./GUI/clientes.tpl', 'w')
            cleanClienteView.write('')
        if clean == "reservas":
            cleanReservaView = open('./GUI/reservas.tpl', 'w')
            cleanReservaView.write('')
        if clean == "comandas":
            cleanComandaView = open('./GUI/comandas.tpl', 'w')
            cleanComandaView.write('')
        for model in objects:
            model.draw()
        return True
