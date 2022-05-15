class Reserva(object):

    def __init__(self, cliente=None, data_reserva=None, data_checkin=None,
                 data_checkout=None, id_reserva=None, id_quarto=None,
                 valor_reserva=None, status=None, tipo_pagamento=None,
                 numero_dias=None, comanda=None, tipo_quarto=None):
        self.__cliente = cliente
        self.__data_reserva = data_reserva
        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout
        self.__id_reserva = id_reserva
        self.__id_quarto = id_quarto
        self.__valor_reserva = valor_reserva
        self.__status = status
        self.__tipo_pagamento = tipo_pagamento
        self.__numero_dias = numero_dias
        self.__comanda = comanda
        self.__tipo_quarto = tipo_quarto

        # Index do iterador
        self.index = 0

        # Campos do iterador
        self.items = ["_Reserva__data_reserva",
                      "_Reserva__data_checkin",
                      "_Reserva__data_checkout",
                      "_Reserva__id_reserva",
                      "_Reserva__id_quarto",
                      "_Reserva__valor_reserva",
                      "_Reserva__status",
                      "_Reserva__tipo_pagamento",
                      "_Reserva__numero_dias",
                      "_Reserva__comanda",
                      "_Reserva__tipo_quarto",
                      "_Reserva__cliente"]

    def __del__(self):
        print 'RIP Reserva'

    # Iterador == 0
    def __iter__(self):
        return self

    # Iterador += 1
    def next(self):
        if self.index < len(self.items):
            self.index += 1
            k = self.items[self.index - 1]
            return (k.replace('_Reserva__', ''), getattr(self, k))
        else:
            # zera o iterador
            self.index = 0
            raise StopIteration

    #Sobrecarga toString
    def __str__(self):
        return str(self.__dict__).replace('_Reserva__', '')

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def draw(self):
        fileIO = open('./GUI/reservas.tpl', 'a')
        for atribute, value in self:
            if not value:
                value = None
            fileIO.write('<p>' + str(atribute.upper()) +
                         ' : <b>' + str(value) +
                         '</b></p>' + '\n')
        fileIO.write('<p>------------------------------------------------</p>\n')
        fileIO.close()

    def getDataReserva(self):
        return self.__data_reserva

    def getDataCheckIn(self):
        return self.__data_checkin

    def getDataCheckOut(self):
        return self.__data_checkout

    def getIdReserva(self):
        return self.__id_reserva

    def getIdQuarto(self):
        return self.__id_quarto

    def getValorReserva(self):
        return self.__valor_reserva

    def getStatus(self):
        return self.__status

    def getTipoPagamento(self):
        return self.__tipo_pagamento

    def getNumeroDias(self):
        return self.__numero_dias

    def getComanda(self):
        return self.__comanda

    def getCliente(self):
        return self.__cliente

    def getTipoQuarto(self):
        return self.__tipo_quarto

    def setDataReserva(self, data_reserva):
        self.__data_reserva = data_reserva
        return True

    def setDataCheckIn(self, data_checkin):
        self.__data_checkin = data_checkin
        return True

    def setDataCheckOut(self, data_checkout):
        self.__data_checkout = data_checkout
        return True

    def setIdReserva(self, id_reserva):
        self.__id_reserva = id_reserva
        return True

    def setIdQuarto(self, id_quarto):
        self.__id_quarto = id_quarto
        return True

    def setValorReserva(self, valor_reserva):
        self.__valor_reserva = valor_reserva
        return True

    def setStatus(self, status):
        self.__status = status
        return True

    def setTipoPagamento(self, tipo_pagamento):
        self.__tipo_pagamento = tipo_pagamento
        return True

    def setNumeroDias(self, numero_dias):
        self.__numero_dias = numero_dias
        return True

    def setComanda(self, comanda):
        self.__comanda = comanda
        return True

    def setTipoQuarto(self, tipo_quarto):
        self.__tipo_quarto = tipo_quarto
        return True

    def setCliente(self, cliente):
        self.__cliente = cliente
        return True
