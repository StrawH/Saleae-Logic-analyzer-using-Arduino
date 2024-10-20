const int signalPin = 2; // Pin where the square wave is connected

volatile unsigned long highTime = 0;  // Time for high pulse
volatile unsigned long lowTime = 0;   // Time for low pulse
volatile unsigned long lastInterruptTime = 0; // Last interrupt time
volatile int pulseCount = 0; // Count of pulses
unsigned long lastPulseTime = 0; // Last pulse time

void setup() {
  Serial.begin(9600);
  pinMode(signalPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(signalPin), handleInterrupt, CHANGE);
}

void loop() {
  // Wait for a few seconds to capture the square wave
  delay(1000);

  // Calculate frequency and duty cycle
  if (pulseCount > 0) {
    float frequency = pulseCount / (millis() / 1000.0); // Frequency in Hz
    float dutyCycle = (float)highTime / (highTime + lowTime) * 100; // Duty cycle in percentage

    // Print the results
    Serial.print("High Time: ");
    Serial.print(highTime);
    Serial.println(" µs");
    
    Serial.print("Low Time: ");
    Serial.print(lowTime);
    Serial.println(" µs");
    
    Serial.print("Duty Cycle: ");
    Serial.print(dutyCycle);
    Serial.println(" %");
    
    Serial.print("Frequency: ");
    Serial.print(frequency);
    Serial.println(" Hz");

    // Reset values for the next measurement
    highTime = 0;
    lowTime = 0;
    pulseCount = 0;
  }
}

void handleInterrupt() {
  unsigned long currentTime = micros();
  
  // Check if the pin is HIGH
  if (digitalRead(signalPin) == HIGH) {
    highTime += currentTime - lastInterruptTime; // Add to high time
    pulseCount++;
  } else {
    lowTime += currentTime - lastInterruptTime; // Add to low time
  }

  lastInterruptTime = currentTime; // Update the last interrupt time
}
