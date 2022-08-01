import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Browser")
        self.setGeometry(200,200, 900,600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)


        self.backButton = QPushButton()
        #tu muszę dać ikone (self.backButton.setIcon(QIcon)'icons/nazwapliku.png')
        toolbar.addWidget(self.backButton)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())