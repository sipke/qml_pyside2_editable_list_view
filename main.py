import sys, model2
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView

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
Add a python thread/timer to demonstrate that updating listview elements does not work from them.
"""
import threading
age = 0
def update():
    print("update in timer\n")
    global age, timer
    import time
    for age in range(5):
        # Unless you re-size the window, these additions will not be updated in QML UI.
        ui.model.addPerson("older me", 20 + age)
        time.sleep(2)
    ui.model.addPerson("last one", 40)


timer = threading.Timer(1.0, update)
timer.start()

sys.exit(myApp.exec_())