#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println("Genesis Watch Booting...");
    Serial.println("MotionOS Genesis firmware started.");
}

void loop() {
    Serial.println("Watch is alive.");
    delay(1000);
}