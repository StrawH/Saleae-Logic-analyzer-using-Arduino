// Define the pin where the digital signal will be read
const int signalPin = 2; // Change this to your input pin number

void setup() {
  // Initialize the digital pin as an input
  pinMode(signalPin, INPUT);
  
  // Start the serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the digital signal from the pin
  int signalValue = digitalRead(signalPin);
  
  // Transmit the signal value via serial port
  Serial.println(signalValue);
  
  // Delay for a short period to avoid flooding the serial port
  delay(500); // Adjust the delay as needed
}
