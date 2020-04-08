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
sys.exit(myApp.exec_())