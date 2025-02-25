import QtQuick 2.15
import QtQuick.Controls 2.15


TabBar {
    // Barre de navigation en haut
    id: tabBar
    width: parent.width

    function getTabColor(is_enabled): string {
        return is_enabled ? "lightblue": "lightgray"
    }

    Button {
        text: "Accueil"
        onClicked: stackView.replace("Home.qml") // Remplace la page actuelle
    }

    TabButton {
        text: "First Page"
        enabled: stackView.currentItem.objectName  !== "first-page"
        background: Rectangle {
            color: getTabColor(enabled)
            radius: 5
        }
        onClicked: stackView.push("FirstPage.qml")
    }

    TabButton {
        text: "Second page"
        enabled: stackView.currentItem.objectName  !== "second-page"
        background: Rectangle {
            color: getTabColor(enabled)
            radius: 5
        }
        onClicked: stackView.push("SecondPage.qml")
    }
}