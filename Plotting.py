import serial
import matplotlib.pyplot as plt
import time

# Configure the serial port and baud rate
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Allow time for the connection to establish

# Lists to hold the data
timestamps = []
values = []

# Create a real-time plot
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(timestamps, values, 'b-')
ax.set_ylim(-0.5, 1.5)  # Set y-axis limits for digital signal
ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal Value')
ax.set_title('Real-time Digital Signal Plot')

start_time = time.time()

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        # Convert the line to an integer
        if line.isdigit():
            value = int(line)
            current_time = time.time() - start_time
            
            # Append the data to the lists
            timestamps.append(current_time)
            values.append(value)
            
            # Update the plot
            ax.clear()
            ax.plot(timestamps, values, 'b-')
            ax.set_ylim(-0.5, 1.5)
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Signal Value')
            ax.set_title('Real-time Digital Signal Plot')
            plt.pause(0.1)  # Pause to update the plot

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()  # Close the serial port
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot
