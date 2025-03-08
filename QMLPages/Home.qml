import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15

Item {
    ColumnLayout {
        anchors.fill: parent
        // Grille pour les blocs MFD
        GridLayout {
            columnSpacing: 0
            rowSpacing: 0
            columns: 2

            Button {
                property bool go_to: true

                text: "SC"
                Layout.fillWidth: true
                Layout.fillHeight: true
                font.pixelSize: 24

                onClicked: stackView.push("StarCitizen/MFDConfigurator.qml")
            }

            Button {
                property bool go_to: true
                text: "DCS"
                Layout.fillWidth: true
                Layout.fillHeight: true
                font.pixelSize: 24

                onClicked: stackView.push("StarCitizen/MFDConfigurator.qml")
            }
        }
    }
}
