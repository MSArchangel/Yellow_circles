import random
import sys
import random
from PyQt5.QtGui import QColor, QPainter
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Жёлтые окружности')

    def run(self):
        self.do_paint = True
        self.x, self.y, self.razmer = random.randrange(10, self.width() - 50), \
                                      random.randrange(10, self.height() - 50), \
                                      random.randrange(10, 50)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor('#ffff00'))
            painter.drawEllipse(self.x, self.y, self.razmer, self.razmer)
            painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
