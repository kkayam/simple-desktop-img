import sys

from PyQt5.QtCore import Qt, QPoint, QObject, QThread, pyqtSignal, QSize, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QColor, QMovie
import websocket
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout)


class cssden(QMainWindow):

    def __init__(self,bg):
        super().__init__()

        vbox = QVBoxLayout()
        
        self.movie = QMovie(bg)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)
        self.setWindowOpacity(0.7)
        self.center()

        widget = QWidget()
        self.background = QLabel(self)
        # self.background.setGeometry(0,0,widget.width(),widget.height())
        self.background.setMovie(self.movie)
        self.movie.start()
        # widget.resize(self.background.size())
        vbox.addWidget(self.background)
        vbox.setContentsMargins(0,0,0,0)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.oldPos = self.pos()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def wheelEvent(self, event):
        opacity = max(self.windowOpacity()+(event.angleDelta().y() / 1020),0.015)
        self.setWindowOpacity(opacity)


if __name__ == '__main__':
    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook 
    app = QApplication(sys.argv)
    ex = cssden(sys.argv[1])

    sys.exit(app.exec_())