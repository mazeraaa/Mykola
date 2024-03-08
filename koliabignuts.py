#mozoeroemzoemrozmoeraoeroamazero
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('mozero')
main_win.show()
line = QHBoxLayout()
title = QLabel('текст')
line.addWidget(title, alignment = Qt.AlignCenter)
main_win.setLayout(line)
app.exec_()