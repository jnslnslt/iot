// libraries for PT100
#include <OneWire.h>
#include <DallasTemperature.h>
// libraries for AM2320B
#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"

OneWire oneWire(4); // set PT100 pin to 4
DallasTemperature pt100(&oneWire);

Adafruit_AM2320 am2320 = Adafruit_AM2320();


void setup() {
  // start serial, pt100 and am2320
  Serial.begin(9600);
  pt100.begin();
  am2320.begin();
  }

void loop() {
  // put your main code here, to run repeatedly:
  pt100.requestTemperatures();
  Serial.print("PT100: "), Serial.println(pt100.getTempCByIndex(0));
  Serial.print("AM2320 T: "), Serial.println(am2320.readTemperature());
  Serial.print("AM2320 H: "), Serial.println(am2320.readHumidity());
  Serial.println();
  delay(2000);

}
