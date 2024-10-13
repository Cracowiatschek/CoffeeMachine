import pywinusb.hid as hid

def find_light_sensor():
    # Zidentyfikuj urządzenie HID
    all_hids = hid.find_all_hid_devices()
    for device in all_hids:
        if device.product_name == 'Your Light Sensor Name':  # Zmień na nazwę swojego czujnika
            return device
    return None

def read_light_data(device):
    # Otwórz urządzenie
    device.open()

    # Odczytaj dane z czujnika
    try:
        while True:
            data = device.read(1)  # Odczytaj 1 bajt danych
            if data:
                print("Light data:", data)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        device.close()

def main():
    sensor = find_light_sensor()
    if sensor:
        print("Found light sensor:", sensor.product_name)
        read_light_data(sensor)
    else:
        print("Light sensor not found.")

if __name__ == '__main__':
    main()
