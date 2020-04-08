import sys, model2
from PySide2.QtCore import QUrl
from PySide2.QtCore import QObject
from PySide2.QtCore import Signal
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView

queued = False  # Change between False and True to test direct (which does not auto update) or queued signal (which does)

class MainWindow(QQuickView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = model2.PersonModel()
        self.rootContext().setContextProperty('PersonModel', self.model)
        self.rootContext().setContextProperty('MainWindow', self)
        self.setSource(QUrl('test2.qml'))

myApp = QApplication(sys.argv)
ui = MainWindow()
ui.show()

"""
Add a python thread/timer to demonstrate that updating listview elements does not work from them unless you used
a queued connection signal.
----------------------------------------------
"""
import threading
age = 0


class Link(QObject):
    """ A class to provide a signal between thread and Qt UI"""
    updateSignal = Signal(str, int)


def update():
    global age, timer, queued
    import time
    link = Link()
    link.updateSignal.connect(ui.model.addPerson, Qt.QueuedConnection)  # This line ...
    for age in range(20, 25):
        if queued:
            print("queued", age)
            link.updateSignal.emit("queued", age)  # ... and this line are the key
        else:
            # Unless you re-size the window, these additions will not be updated in QML UI.
            print("direct", age)
            ui.model.addPerson("direct", age)
        time.sleep(2)
    ui.model.addPerson("last one", 40)


timer = threading.Timer(1.0, update)
timer.start()

sys.exit(myApp.exec_())