#include <OneWire.h>
#include <DallasTemperature.h>

OneWire oneWire(4); // set pin to 4
DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  Serial.println(sensors.getTempCByIndex(0));
  delay(50);
}

