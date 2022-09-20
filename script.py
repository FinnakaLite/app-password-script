import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.getText()
 
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Password:", QLineEdit.Normal, "")
        if okPressed and text != '':
            if text == "password":
                print("Correct!")
                sys.exit(0)
            else:
                print("Incorrect password!")
                sys.exit(1)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())