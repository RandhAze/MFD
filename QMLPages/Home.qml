import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    Column {
        anchors.centerIn: parent
        spacing: 20

        Button {
            text: "Star Citizen"
            onClicked: stackView.push("Home.qml")  // Charge la première page du lot 1
        }

        Button {
            text: "DCS"
            onClicked: stackView.push("Home.qml")  // Charge la première page du lot 1
        }

        Button {
            text: "Test"
            onClicked: stackView.push("Test/FirstPage.qml")  // Charge la première page du lot 2
        }
    }
}
