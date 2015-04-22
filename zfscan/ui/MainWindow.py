import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MainWindow:
    def __init__(self, width, height):
        app = QApplication([])
        mainWidget = QWidget()
        layout = QVBoxLayout(mainWidget)
        label = QLabel("<font color=red size=40>Hello, World!</font>")
        layout.addWidget(label)
        mainWidget.resize(width, height)
        mainWidget.show()
        sys.exit(app.exec_())