from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButon, QLineEdit
from PyQt5.QtCore import Qt

class MainWin(QWidget):
    def __init__(self):
        self.set_appear()
        self.ininUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.resize(600,400)
        self.setWindowTitle('Инструкция')
        self.move(250,250)

    def ininUI(self):
        hello = QLabel('здесь будет приветствие')
        instr = QLabel('здесь будет инструкция')
        button = QPushButon('начать')
        v_line = QVBoxLayout
    def connects(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    main = MainWin()
    app.exec_()
