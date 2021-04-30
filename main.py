from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller import Controller
import sys

if __name__ == "__main__":
   app  = QApplication(sys.argv)
   Window = QMainWindow()
   ui = Controller()
   ui.setupUi(Window)
   ui.controller()
   Window.show()
   print("123123123")
   sys.exit(app.exec_())
