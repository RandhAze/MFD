import sys
from PyQt6.QtWidgets import QApplication
from InputDetector import InputDetector
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen_name = "MPI7002"
    input_detector = InputDetector()
    input_detector.configure(screen_name)  # ⚠️ Change le nom du périphérique si nécessaire

    window = MainWindow(input_detector, screen_name)
    window.show()

    sys.exit(app.exec())
