from Utils.factory import Factory


def build(tipo):
    return Factory().create(tipo)
