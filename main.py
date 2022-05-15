from Controller.controller_api import createController
from GUI.gui_api import *

####################################################Unit Tests##########################################################

#Create methods---------------------------------------------------------------------------------------------------------
assert createController(), 'Fail'
assert createController().create('cliente'), 'Fail'
assert createController().create('comanda'), 'Fail'
assert createController().create('reserva'), 'Fail'
assert createController().create('view'), 'Fail'

#Set data methods-------------------------------------------------------------------------------------------------------
#Clientes class
assert createController().clientes[0].setNome('SAMUEL CARLOS'), 'Fail'
assert createController().clientes[0].setCPF('111.222.333-44'), 'Fail'
assert createController().clientes[0].setIdade(29), 'Fail'
assert createController().clientes[0].setEmail("email@gmail.com"), 'Fail'
assert createController().clientes[0].setTelefone("+55 31 123456789"), 'Fail'
assert createController().clientes[0].setCidade("EGER"), 'Fail'
assert createController().clientes[0].setPais("HUNGARY"), 'Fail'
assert createController().clientes[0].setRua("LEANYKA"), 'Fail'
assert createController().clientes[0].setBairro("HEVES"), 'Fail'
assert createController().clientes[0].setNumero(2), 'Fail'

#Reservas class
assert createController().reservas[0].setCliente(createController().clientes[0]), 'Fail'
assert createController().reservas[0].setDataReserva('31/11/2017'), 'Fail'
assert createController().reservas[0].setDataCheckIn('01/12/2017'), 'Fail'
assert createController().reservas[0].setDataCheckOut('05/12/2017'), 'Fail'
assert createController().reservas[0].setIdReserva(1), 'Fail'
assert createController().reservas[0].setIdQuarto("A-200"), 'Fail'
assert createController().reservas[0].setValorReserva('HUF 10.000 '), 'Fail'
assert createController().reservas[0].setStatus('CLOSED'), 'Fail'
assert createController().reservas[0].setTipoPagamento('MASTERCARD'), 'Fail'
assert createController().reservas[0].setNumeroDias(4), 'Fail'
assert createController().reservas[0].setComanda(createController().comandas[0]), 'Fail'
assert createController().reservas[0].setTipoQuarto("STANDARD SUITE"), 'Fail'

#Comandas class
assert createController().comandas[0].setCodigo("0001"), 'Fail'
assert createController().comandas[0].setQuantidadeBebida("3"), 'Fail'
assert createController().comandas[0].setBebida(['Red Bull', 'Coca Cola 500ml', 'Heineken 350ml']), 'Fail'
assert createController().comandas[0].setQuantidadeAlimento("2"), 'Fail'
assert createController().comandas[0].setAlimento(['Chocolate', 'Cookies']), 'Fail'
assert createController().comandas[0].setValor("HUF 6000"), 'Fail'

#Get data methods-------------------------------------------------------------------------------------------------------
#Clientes class
assert createController().clientes[0].getNome(), 'Fail'
assert createController().clientes[0].getCPF(), 'Fail'
assert createController().clientes[0].getIdade(), 'Fail'
assert createController().clientes[0].getEmail(), 'Fail'
assert createController().clientes[0].getTelefone(), 'Fail'
assert createController().clientes[0].getCidade(), 'Fail'
assert createController().clientes[0].getPais(), 'Fail'
assert createController().clientes[0].getRua(), 'Fail'
assert createController().clientes[0].getBairro(), 'Fail'
assert createController().clientes[0].getNumero(), 'Fail'

#Reservas class
assert createController().reservas[0].getCliente(), 'Fail'
assert createController().reservas[0].getDataReserva(), 'Fail'
assert createController().reservas[0].getDataCheckIn(), 'Fail'
assert createController().reservas[0].getDataCheckOut(), 'Fail'
assert createController().reservas[0].getIdReserva(), 'Fail'
assert createController().reservas[0].getIdQuarto(), 'Fail'
assert createController().reservas[0].getValorReserva(), 'Fail'
assert createController().reservas[0].getStatus(), 'Fail'
assert createController().reservas[0].getTipoPagamento(), 'Fail'
assert createController().reservas[0].getNumeroDias(), 'Fail'
assert createController().reservas[0].getComanda(), 'Fail'
assert createController().reservas[0].getTipoQuarto(), 'Fail'

#Comandas class
assert createController().comandas[0].getCodigo(), 'Fail'
assert createController().comandas[0].getQuantidadeBebida(), 'Fail'
assert createController().comandas[0].getBebida(), 'Fail'
assert createController().comandas[0].getQuantidadeAlimento(), 'Fail'
assert createController().comandas[0].getAlimento(), 'Fail'
assert createController().comandas[0].getValor(), 'Fail'

#Clone data methods-----------------------------------------------------------------------------------------------------
assert createController().clone('cliente', createController().clientes[0]), 'Fail'
assert createController().clone('reserva', createController().reservas[0]), 'Fail'
assert createController().clone('comanda', createController().comandas[0]), 'Fail'

#Draw methods-----------------------------------------------------------------------------------------------------------
assert createController().views[0].draw(createController().clientes, 'clientes'), 'Fail'
assert createController().views[0].draw(createController().reservas, 'reservas'), 'Fail'
assert createController().views[0].draw(createController().comandas, 'comandas'), 'Fail'

#Start GUI--------------------------------------------------------------------------------------------------------------
assert initGUI().run(), 'Fail'
