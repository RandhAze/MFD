from PyQt6.QtCore import QThread, pyqtSignal
import usb.core
import usb.util
from usb.backend import libusb1


class InputDetector(QThread):
    input_detected = pyqtSignal(list)  # Signal pour envoyer les données

    def __init__(self):
        super().__init__()
        self.running = False
        self.previous_event = 0
        self.device = None
        self.endpoint_in = None

    def configure(self, device_name: str) -> None:
        vid, pid = self.get_device_by_name(device_name)

        if vid is None or pid is None:
            raise ValueError("❌ Périphérique non trouvé")

        backend = usb.backend.libusb1.get_backend()
        self.device = usb.core.find(idVendor=vid, idProduct=pid, backend=backend)

        if self.device is None:
            raise ValueError("❌ Périphérique non trouvé")
        
        print("✅ Périphérique trouvé !")

        self.device.set_configuration()
        cfg = self.device.get_active_configuration()
        interface = cfg[(0, 0)]  # Interface 0, alternative setting 0

        for ep in interface:
            if usb.util.endpoint_direction(ep.bEndpointAddress) == usb.util.ENDPOINT_IN:
                self.endpoint_in = ep
                break

        if not self.endpoint_in:
            raise ValueError("⚠ Aucun endpoint IN trouvé !")

    def get_device_by_name(self, device_name: str):
        devices = usb.core.find(find_all=True)

        for device in devices:
            try:
                if usb.util.get_string(device, device.iProduct) == device_name:
                    return device.idVendor, device.idProduct
            except Exception as e:
                print(f"⚠ Erreur lors de l'accès au périphérique : {e}")

        return None, None

    def run(self):
        self.running = True
        while self.running:
            data = self.read_touch_input()
            self.input_detected.emit(data)

    def stop(self):
        self.running = False

    def read_touch_input(self):
        if not self.device or not self.endpoint_in:
            return [0, 0]

        try:
            data = self.device.read(self.endpoint_in.bEndpointAddress, self.endpoint_in.wMaxPacketSize, timeout=100)

            if data[1] == 1 and self.previous_event == 0:
                self.previous_event = 1
                print(f"📥 Données reçues: {data}")
                return [int(data[3]) + int(data[4]) * 256, int(data[5]) + int(data[6]) * 256]

            if data[1] == 0 and self.previous_event == 1:
                self.previous_event = 0

            return [0, 0]
        except usb.core.USBError as e:
            if e.errno == 10060:  # Timeout
                return [0, 0]
            print(f"❌ Erreur USB: {e}")
            return [0, 0]
