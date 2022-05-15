from threading import Thread
from GUI.gui import init


def initGUI():
    gui = Thread(target=init, args=())
    return gui
