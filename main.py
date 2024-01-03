import serial

def parse_message(data):
    header = data[1:3]
    index = data[3]
    yaw = int.from_bytes(data[4:6], byteorder='little', signed=True) * 0.01
    pitch = int.from_bytes(data[6:8], byteorder='little', signed=True) * 0.01
    roll = int.from_bytes(data[8:10], byteorder='little', signed=True) * 0.01
    x_acceleration = int.from_bytes(data[10:12], byteorder='little', signed=True)
    y_acceleration = int.from_bytes(data[12:14], byteorder='little', signed=True)
    z_acceleration = int.from_bytes(data[14:16], byteorder='little', signed=True)
    csum = data[0]

    # Calculate the checksum
    calculated_csum = sum(data[1:18]) & 0xFF

    if header == b'\xaa\xaa':
        return {
            'Header': header,
            'Index': index,
            'Yaw': yaw,
            'Pitch': pitch,
            'Roll': roll,
            'X-acceleration': x_acceleration,
            'Y-acceleration': y_acceleration,
            'Z-acceleration': z_acceleration,
            'Checksum': csum
        }
    else:
        return None

def main():
    serial_port = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1)  # Replace 'COM1' with your actual port

    while True:
        # Read 19 bytes from the serial port
        data = serial_port.read(19)

        if len(data) == 19:
            parsed_data = parse_message(data)
            
            if parsed_data:
                print("True :", parsed_data['Yaw'])
            else:
                print("False :", data[1:3])

if __name__ == "__main__":
    main()
