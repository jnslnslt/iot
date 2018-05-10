// Arduino program to read
// - DS18B20 PT100 temperature sensor
// - AM2320B temperature&humidity sensor
// print readings to serial and send via rf using radiohead library
// and 433mhz ASK transmitter

// Jani Sulunsilta
// last modified 11.5.2018

// libraries for DS18B20
#include <OneWire.h>
#include <DallasTemperature.h>
// libraries for AM2320B
#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"
// libraries for ASK transmitter
#include <RH_ASK.h>
#include <SPI.h> // not used but needed to compile

OneWire oneWire(4); // set PT100 pin to 4
DallasTemperature pt100(&oneWire);

Adafruit_AM2320 am2320 = Adafruit_AM2320(); // yellow to SDA/A4, whit to SCL/A5

RH_ASK driver; // default tx=12, rx=11

void setup() {
  // start serial, pt100 and am2320
  Serial.begin(9600);
  pt100.begin();
  am2320.begin();
  // start rf driver
  if (!driver.init())
    Serial.println("init failed");
  
  }

void loop() {
  // put your main code here, to run repeatedly:

  float data[3];

  // Read pt100 temp
  pt100.requestTemperatures();
  data[0] = pt100.getTempCByIndex(0);
  Serial.print("PT100: "), Serial.println(data[0]);

  // Read am2320 temp
  data[1] = am2320.readTemperature();
  Serial.print("AM2320 T: "), Serial.println(data[1]);

  // Read am2320 humidity
  data[2] = am2320.readHumidity();
  Serial.print("AM2320 H: "), Serial.println(data[2]);

  // Send readings via rf
  driver.send((uint8_t *)&data, sizeof(data));
  driver.waitPacketSent();

  // delay, am2320 max sample rate 0.5Hz
  delay(2000);

} 
