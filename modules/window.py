from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit
from .app import app

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

main_window = QMainWindow()
main_window.setGeometry(100, 100, WIDTH_WINDOW, HEIGHT_WINDOW)
main_window.setStyleSheet("background-color: #333333;")

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

central = QWidget(parent=main_window)
main_window.setCentralWidget(central)

window_layout = QVBoxLayout()
window_layout.setContentsMargins(10, 40, 10, 40)
window_layout.setSpacing(55)
central.setLayout(window_layout)


def click():
    print("click")


def enter_text(text):
    print(text)


row_button = QHBoxLayout()

button = QPushButton(text="Press")
button.setFixedSize(100, 42)
button.setStyleSheet("color: white; background-color: #4a4a4a; border: 1px solid #555555;")
button.clicked.connect(click)

row_button.addWidget(button)
row_button.addStretch()
window_layout.addLayout(row_button)

row_frame = QHBoxLayout()

frame = QFrame()
frame.setStyleSheet("background-color: #808080;")
frame.setFixedSize(500, 505)

frame_layout = QHBoxLayout()
frame.setLayout(frame_layout)

main = QComboBox()
main.addItems(["Опція 1", "Опція 2", "Опція 3"])
main.setStyleSheet("color: white; background-color: #808080;")
frame_layout.addWidget(main)

linein = QLineEdit()
linein.setPlaceholderText("Введи текст")
linein.setStyleSheet("color: white; background-color: #0d0d0d;")
linein.textChanged.connect(enter_text)
frame_layout.addWidget(linein)

row_frame.addWidget(frame)
row_frame.addStretch()
window_layout.addLayout(row_frame)

window_layout.addStretch()