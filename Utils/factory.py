from Models.model_api import criaCliente, criaComanda, criaReserva, comparaReservas, comparaClientes
from Views.view_api import createView


#Method Factory
class Factory(object):
    def __init__(self):
        pass

    def create(self, model):
        if model == "cliente":
            return criaCliente()
        if model == "reserva":
            return criaReserva()
        if model == "comanda":
            return criaComanda()
        if model == "view":
            return createView()
        assert 0, "Nao existe o tipo: " + type

    def compare(self, model, object1, object2):
        if model == "clientes":
            return comparaClientes(object1, object2)
        if model == "reservas":
            return comparaReservas(object1, object2)
        assert 0, "Nao existe o tipo: " + model
