from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project F1")

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setStyleSheet("""
        QWidget{
            background-color: rgba(20,20,20,220);
            border:2px solid #00D2FF;
            border-radius:15px;
            color:white;
        }

        QLabel{
            color:white;
        }
        """)

        self.resize(330, 260)

        self.move(40, 40)

        layout = QVBoxLayout()

        title = QLabel("🏎 PROJECT F1")
        title.setFont(QFont("Bahnschrift", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.speed = QLabel("Speed : 0 km/h")
        self.gear = QLabel("Gear : N")
        self.rpm = QLabel("RPM : 0")
        self.drs = QLabel("DRS : OFF")

        font = QFont("Bahnschrift", 12)

        self.speed.setFont(font)
        self.gear.setFont(font)
        self.rpm.setFont(font)
        self.drs.setFont(font)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.speed)
        layout.addWidget(self.gear)
        layout.addWidget(self.rpm)
        layout.addWidget(self.drs)

        self.setLayout(layout)

    def update_data(self, game_state):

        self.speed.setText(f"Speed : {game_state.speed} km/h")
        self.gear.setText(f"Gear : {game_state.gear}")
        self.rpm.setText(f"RPM : {game_state.rpm}")
        self.drs.setText(
            f"DRS : {'ON' if game_state.drs else 'OFF'}"
        )