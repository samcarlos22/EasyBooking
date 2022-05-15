import copy
from Utils.factory_api import build


#Singleton
class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class Controller(object):
    __metaclass__ = SingletonType

    def __init__(self):
        self.reservas = []
        self.clientes = []
        self.comandas = []
        self.views = []

    def __del__(self):
        print 'RIP Controller'

    def create(self, tipo):
        if tipo == 'reserva':
            self.reservas.append(build(tipo))
            return True
        if tipo == 'cliente':
            self.clientes.append(build(tipo))
            return True
        if tipo == 'comanda':
            self.comandas.append(build(tipo))
            return True
        if tipo == 'view':
            self.views.append(build(tipo))
            return True
        print "Nao existe esse tipo"
        return False

    def clone(self, tipo, source):
        if tipo == 'reserva':
            destination = copy.copy(source)
            self.reservas.append(destination)
            return True
        if tipo == 'cliente':
            destination = copy.copy(source)
            self.clientes.append(destination)
            return True
        if tipo == 'comanda':
            destination = copy.copy(source)
            self.comandas.append(destination)
            return True
        if tipo == 'view':
            destination = copy.copy(source)
            self.views.append(destination)
            return True
        print "Nao existe esse tipo"
        return False
