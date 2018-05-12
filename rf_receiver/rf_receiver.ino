// 433Mhz receiver using RadioHead library
// print catched messages to serial
#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile
RH_ASK driver;
void setup()
{
    Serial.begin(9600); // Debugging only
    if (!driver.init())
         Serial.println("init failed");

}
void loop()
{
  
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
  uint8_t buflen = sizeof(buf); 
  if (driver.recv(buf, &buflen)) // Non-blocking
  {
      // Message with a good checksum received, dump it.
      //Serial.write(buf, buflen); // print message to serial
      float data[4];
      memcpy(data,buf,sizeof(buf));
      Serial.print(data[0],0);
      Serial.print(" ");
      for (byte i=1; i <= 3; i++) {
        Serial.print(data[i]);
        Serial.print(" ");
      }
      Serial.println();
  }
}
