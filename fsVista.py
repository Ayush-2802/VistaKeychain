import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,300,1500,700)
    win.setWindowTitle("Vista Password Manager")
    win.setWindowIcon(QIcon("titleicon.jpg"))
    win.show()
    sys.exit(app.exec_())

window()