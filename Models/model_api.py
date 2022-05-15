"""This is the model API that communicates with the controller."""

from Models.model_cliente import Cliente
from Models.model_reserva import Reserva
from Models.model_comanda import Comanda


def criaCliente(nome=None, cpf=None, idade=None, email=None, telefone=None, cidade=None,
                pais=None, rua=None, bairro=None, numero=None):
    cliente = Cliente(nome, cpf, idade, email, telefone, cidade, pais, rua, bairro, numero)
    return cliente


def comparaClientes(cliente, cliente2):
    return cliente == cliente2


def criaReserva(data_reserva=None, data_checkin=None, data_checkout=None, id_reserva=None,
                id_quarto=None, valor_reserva=None, status=None, tipo_pagamento=None,
                numero_dias=None, comanda=None, tipo_quarto=None):
    reserva = Reserva(data_reserva, data_checkin, data_checkout, id_reserva, id_quarto,
                      valor_reserva, status, tipo_pagamento, numero_dias, comanda, tipo_quarto)
    return reserva


def criaComanda(valor=None, codigo=None, bebida=None, alimento=None, quantidade_bebida=None,
                quantidade_alimento=None):

    comanda = Comanda(valor, codigo, bebida, alimento, quantidade_bebida, quantidade_alimento)
    return comanda


def comparaReservas(reserva, reserva2):
    return reserva == reserva2


def comparaComandas(comanda, comanda2):
    return comanda == comanda2
