import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MainWindow:
    def __init__(self, width, height):
        app = QApplication([])
        main_window = QWidget()

        self.label = QLabel("<font color=red size=40>Push Button for something fun!</font>")
        self.button1 = QPushButton("Push Me!")

        main_window.setLayout(self.build_layout([self.label, self.button1]))
        main_window.resize(width, height)
        main_window.show()
        sys.exit(app.exec_())

    def build_layout(self, widgets):
        layout = QVBoxLayout()
        for i in widgets:
            layout.addWidget(i)
        return layout

    def update_label(self):
        """"""