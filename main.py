import serial

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
from math import radians

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
    
def visualize_orientation(roll, pitch, yaw):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Orientation Visualization')

    # Define rotation matrix for yaw, pitch, and roll
    R = np.array([[np.cos(yaw)*np.cos(pitch), np.cos(yaw)*np.sin(pitch)*np.sin(roll) - np.sin(yaw)*np.cos(roll), np.cos(yaw)*np.sin(pitch)*np.cos(roll) + np.sin(yaw)*np.sin(roll)],
                  [np.sin(yaw)*np.cos(pitch), np.sin(yaw)*np.sin(pitch)*np.sin(roll) + np.cos(yaw)*np.cos(roll), np.sin(yaw)*np.sin(pitch)*np.cos(roll) - np.cos(yaw)*np.sin(roll)],
                  [-np.sin(pitch), np.cos(pitch)*np.sin(roll), np.cos(pitch)*np.cos(roll)]])

    # Define axis vectors
    axis_length = 1.0
    x_axis = R.dot(np.array([axis_length, 0, 0]))
    y_axis = R.dot(np.array([0, axis_length, 0]))
    z_axis = R.dot(np.array([0, 0, axis_length]))

    # Plot axis vectors
    ax.quiver(0, 0, 0, x_axis[0], x_axis[1], x_axis[2], color='r', label='X-axis')
    ax.quiver(0, 0, 0, y_axis[0], y_axis[1], y_axis[2], color='g', label='Y-axis')
    ax.quiver(0, 0, 0, z_axis[0], z_axis[1], z_axis[2], color='b', label='Z-axis')

    ax.legend()

    plt.show()

def main():
    serial_port = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1)  # Replace 'COM1' with your actual port

    while True:
        # Read 19 bytes from the serial port
        data = serial_port.read(19)

        if len(data) == 19:
            parsed_data = parse_message(data)
            
            if parsed_data:
                print("True :", parsed_data['Yaw'])
                visualize_orientation(parsed_data['Roll'], parsed_data['Pitch'], parsed_data['Yaw'])
            else:
                print("False :", data[1:3])

if __name__ == "__main__":
    main()
