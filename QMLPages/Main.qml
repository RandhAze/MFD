import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 800
    height: 600

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: "Home.qml"  // Charge la page principale au démarrage
    }
}
