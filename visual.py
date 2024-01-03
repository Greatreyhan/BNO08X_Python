import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
from math import radians

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

# Example usage
roll = radians(20.85)  # Replace with your actual roll angle
pitch = radians(-1.10)  # Replace with your actual pitch angle
yaw = radians(0.01)  # Replace with your actual yaw angle

visualize_orientation(roll, pitch, yaw)
