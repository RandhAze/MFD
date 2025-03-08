import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtQuickWidgets import QQuickWidget
from PyQt6.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self, input_detector, screen_name: str):
        super().__init__()

        self.input_detector = input_detector
        self.init_ui(screen_name)

        # Connexion du signal du détecteur d'entrée
        self.input_detector.input_detected.connect(self.handle_input)
        self.input_detector.start()

    def init_ui(self, screen_name):
        app = QApplication.instance()
        touchscreen = None

        for screen in app.screens():
            if screen.name() == screen_name:
                touchscreen = screen

        if touchscreen == None:
            raise ValueError("❌ Ecran non trouvé")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Création du QQuickWidget pour le QML
        qml_widget = QQuickWidget()
        qml_widget.engine().addImportPath(sys.path[0])
        qml_widget.setSource(QUrl("QMLPages/Main.qml"))
        qml_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        layout.addWidget(qml_widget)

        self.setWindowTitle("MFD")

        # deplacement de l'application sur l'ecran choisi
        self.move(touchscreen.geometry().x(), touchscreen.geometry().y())
        self.showFullScreen()

    def handle_input(self, data):
        if data == [0, 0]:
            return
        
        self.find_widget_at_position(self, *data)

    def closeEvent(self, event):
        self.input_detector.stop()
        self.input_detector.wait()
        event.accept()

    def find_widget_at_position(self, widget, x, y):
        child = widget.childAt(x, y)

        if not child:
            return widget

        # Vérifier si c'est un QQuickWidget
        if isinstance(child, QQuickWidget):
            root_object = child.rootObject()

            if not root_object:
                return child

            self.find_qml_item_at(root_object, x - child.x(), y - child.y())
            return

        child_x = x - child.x()
        child_y = y - child.y()

        return self.find_widget_at_position(child, child_x, child_y)

    def find_qml_item_at(self, object, x, y):
        if object.property("step_input"):
            print("step input")

        if object.property("go_to"):
            object.clicked.emit()
            return

        if object.property("final_input"):
            print("finale input")
            return

        child_qml = object.childAt(x, y)

        if not child_qml:
            return

        child_x = x - child_qml.x()
        child_y = y - child_qml.y()

        self.find_qml_item_at(child_qml, child_x, child_y)
