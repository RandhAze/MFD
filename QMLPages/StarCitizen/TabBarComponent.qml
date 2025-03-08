import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15

Rectangle {
    Layout.fillWidth: true
    Layout.preferredHeight: 50
    color: "lightgray"

    function getTabColor(is_enabled): string {
        return is_enabled ? "lightblue" : "lightgray";
    }

    Row {
        anchors.fill: parent  // 🔹 S'étend sur tout le Rectangle
        spacing: 10  // 🔹 Ajoute un espacement entre les boutons

        TabButton {
            text: "Accueil"
            height: parent.height
            width: parent.width * 0.25

            background: {
                color: getTabColor(enabled);
                radius: 5;
            }

            onClicked: stackView.replace("../Home.qml") // Remplace la page actuelle
        }

        TabButton {
            text: "MFD"
            enabled: stackView.currentItem.objectName !== "MFD-configurator"
            height: parent.height
            width: parent.width * 0.25

            background: {
                color: getTabColor(enabled);
                radius: 5;
            }

            onClicked: stackView.push("MFFConfigurator.qml")
        }
    }
}
