import numpy as np
import matplotlib.pyplot as plt
import time

# Parameters for the pulse signal
duration = 10  # Duration of the signal in seconds
sampling_rate = 100  # Samples per second
frequency = 1  # Frequency of the pulse in Hz
pulse_width = 0.5  # Width of the pulse in seconds

# Generate time values
t = np.arange(0, duration, 1 / sampling_rate)

# Initialize the signal array
signal = np.zeros(len(t))

# Generate the pulse signal
for i in range(len(t)):
    if (t[i] % (1 / frequency)) < pulse_width:
        signal[i] = 1

    # Update the plot
    plt.clf()  # Clear the current figure

    # Simplified plot command
    current_time = t[:i + 1]
    current_signal = signal[:i + 1]
    plt.plot(current_time, current_signal, 'b-', drawstyle='steps-post')

    plt.ylim(-0.5, 1.5)
    plt.xlim(0, duration)
    plt.xlabel('Time (s)')
    plt.ylabel('Signal Value')
    plt.title('Real-time Pulse Waveform')
    plt.pause(0.01)  # Pause to create a real-time effect

plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final plot
