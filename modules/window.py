import random

from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit
from .app import app

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

main_window = QMainWindow()
main_window.setWindowTitle("Генератор паролів")
main_window.setGeometry(100, 100, WIDTH_WINDOW, HEIGHT_WINDOW)
main_window.setStyleSheet("background-color: #c18bfb; color: #1a1a1a;")

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

central = QWidget(parent=main_window)
main_window.setCentralWidget(central)

window_layout = QVBoxLayout()
window_layout.setContentsMargins(10, 40, 10, 40)
central.setLayout(window_layout)

CONTROL_STYLE = "color: #1a1a1a; background-color: #c18bfb; border: 1px solid #5b3a99;"


def click():
    print("click")


def enter_text(text):
    print(text)


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '?', '-', '_']


def generate():
    length = [6, 8, 12, 16][length_combo.currentIndex()]
    kind = type_combo.currentIndex()
    if kind == 0:
        chars = digits
    elif kind == 1:
        chars = letters + digits
    else:
        chars = letters + digits + symbols
    password = ""
    for _ in range(length):
        item = random.choice(chars)
        password += item
    linein.setText(password)
#CurrentIndex - показывает индекс выбраного лемнта
#sEtText - устанавливает ткст в виджет


def clear():
    linein.clear()
#.clear- чистт віджет

row = QHBoxLayout()
row.setSpacing(10)

length_combo = QComboBox()
length_combo.addItems(["6", "8", "12", "16"])
length_combo.setFixedHeight(24)
length_combo.setStyleSheet("color: #1a1a1a; background-color: #99ccff; border: 1px solid #5b3a99;")
row.addWidget(length_combo)

type_combo = QComboBox()
type_combo.addItems(["Тільки цифри", "Літери та цифри", "Усі символи"])
type_combo.setFixedHeight(24)
type_combo.setStyleSheet(CONTROL_STYLE)
row.addWidget(type_combo)

button = QPushButton(text="Згенерувати")
button.setFixedHeight(26)
button.setStyleSheet(CONTROL_STYLE)
button.clicked.connect(generate)
row.addWidget(button)

frame = QFrame()
frame.setStyleSheet("background-color: #c18bfb; border: 1px solid #8a5fd0;")
frame.setFixedSize(230, 100)

frame_layout = QHBoxLayout()
frame_layout.setContentsMargins(4, 4, 4, 4)
frame.setLayout(frame_layout)

linein = QLineEdit()
linein.setStyleSheet("color: #1a1a1a; background-color: transparent; border: none;")
linein.textChanged.connect(enter_text)
frame_layout.addWidget(linein)

row.addWidget(frame)

clear_button = QPushButton(text="Очистити")
clear_button.setFixedHeight(26)
clear_button.setStyleSheet(CONTROL_STYLE)
clear_button.clicked.connect(clear)
row.addWidget(clear_button)

window_layout.addStretch()
window_layout.addLayout(row)
window_layout.addStretch()