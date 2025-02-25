import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Application"

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: "Home.qml"  // On démarre sur la page d'accueil
    }
}