import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15

ColumnLayout {
    objectName: "MFD-configurator"
    // Barre de navigation
    TabBarComponent {}
    
    GridLayout {
        width: parent.width
        height: parent.height

        columnSpacing: 0
        rowSpacing: 0
        columns: 2
        Repeater {
            
            model: ["MFD1", "MFD2", "MFD3", "MFD4"]
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                radius: 10
                border.color: "blue"
                border.width: 1
                color: "transparent"
                property string step_input: "step"
               
                GridLayout {
                    anchors.fill: parent
                    columns: 2
                    Layout.fillWidth: true
                    columnSpacing: 0
                    rowSpacing: 0

                    Repeater {
                        // TODO nb Ecrans
                        model: ["Self Status", "Target status", "Scanning", "Communication", "IFCS", "Diagnostics", "Ressource Network"]

                        Button {
                            text: modelData
                            property string final_input: "final"
                            Layout.fillWidth: true
                            Layout.fillHeight: true
                            font.pixelSize: 24
                            onClicked: console.log(text)
                        }
                    }
                }
            }
        }
    }
}
