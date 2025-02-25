import QtQuick 2.15
import QtQuick.Controls 2.15

Page {
    title: "First page"
    objectName: "first-page"
    
    // Barre de navigation en haut
    header: TabBarComponent {}

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Bienvenue sur la première page du Lot TEST"
            font.pixelSize: 20
        }
    }
}
