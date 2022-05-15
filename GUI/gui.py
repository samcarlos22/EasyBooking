from bottle import route, run, template


@route('/clientes/')
def clientes_observer():
    return template('./GUI/clientes.tpl')


@route('/reservas/')
def reservas_observer():
    return template('./GUI/reservas.tpl')


@route('/comandas/')
def comandas_observer():
    return template('./GUI/comandas.tpl')


def init():
    return run(host='localhost', port=8080, reloader=True, debug=True, quiet=True)
