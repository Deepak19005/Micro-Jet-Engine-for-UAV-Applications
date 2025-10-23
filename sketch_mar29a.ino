#include <Servo.h>

Servo esc;
int currentPulseWidth = 1000; // last saved speed

void setup() {
  esc.attach(9);
  Serial.begin(9600);

  Serial.println("--- Motor Controller Ready ---");

  // Arming sequence
  esc.writeMicroseconds(2000);
  delay(2000);
  esc.writeMicroseconds(1000);
  delay(2000);

  Serial.println("ESC Armed! Enter speed (0-100):");
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // read until Enter
    int speed = input.toInt();                   // convert to number

    if (input.length() > 0) {
      speed = constrain(speed, 0, 100);
      int targetPulseWidth = map(speed, 0, 100, 1000, 2000);

      if (speed == 0) {
        // 🚨 Sudden stop
        currentPulseWidth = 1000;
        esc.writeMicroseconds(currentPulseWidth);
        Serial.println("Motor STOPPED suddenly!");
      } else {
        Serial.print("Changing speed smoothly to: ");
        Serial.println(speed);
        setSpeedSmooth(targetPulseWidth); // smooth ramp for >0
      }
    }
  }

  // Keep sending last speed
  esc.writeMicroseconds(currentPulseWidth);
  delay(20);
}

// Smooth acceleration/deceleration function
void setSpeedSmooth(int targetPulse) {
  while (currentPulseWidth != targetPulse) {
    if (currentPulseWidth < targetPulse) currentPulseWidth++;
    else currentPulseWidth--;
    esc.writeMicroseconds(currentPulseWidth);
    delay(5); // controls smoothness
  }
}