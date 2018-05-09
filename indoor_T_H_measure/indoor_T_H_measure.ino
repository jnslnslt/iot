#include "Adafruit_AM2320.h"

Adafruit_AM2320 am2320 = Adafruit_AM2320();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  am2320.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(am2320.readTemperature());
  Serial.println(am2320.readHumidity());
  Serial.println();

  delay(2000);
}
