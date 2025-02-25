import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import constants

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])
    
    context = engine.rootContext()
    
    context.setContextProperty("windowWidth", constants.X_RESOLUTION)
    context.setContextProperty("windowHeight", constants.Y_RESOLUTION)


    engine.loadFromModule("QMLPages", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)