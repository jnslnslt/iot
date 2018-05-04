// ASK transmitter with RadioHead library
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
RH_ASK driver; // default pins 11 receive, 12 send, 10 ??
void setup()
{
    Serial.begin(9600);   // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}
void loop()
{
    const char *msg = "hello";
    driver.send((uint8_t *)msg, strlen(msg));
    driver.waitPacketSent();
    delay(200);
}
