import serial

def read_ftdi_data(baudrate=115200, timeout=1):
    try:
        # Open the serial port
        ser = serial.Serial('/dev/ttyUSB0', baudrate, timeout=timeout)
        print(f"Connected to {ser.name}")

        while True:
            # Read a chunk of data
            data = ser.read(19)  # Adjust the size according to your message size
            if data:
                # Process the received data
                parse_uart_data(data)

    except serial.SerialException as e:
        print(f"Error: {e}")
    finally:
        # Close the serial port when done
        ser.close()

def parse_uart_data(data):
    # Your parsing code here
    print(f"Received data: {data}")

# Replace 'COMx' with the actual COM port your FTDI device is connected to
read_ftdi_data()
