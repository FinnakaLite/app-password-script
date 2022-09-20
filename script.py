import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Input'
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
                subprocess.call(
                    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/VLC.app"]
                    )
                sys.exit(0)
            else:
                print("Error")
                sys.exit(0)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())