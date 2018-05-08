// Set IO pins
const int moistureSensorPin = A0;
const int pumpControlPin = 7;

// Set minimum interval between pumping sequences (milliseconds)
const unsigned long minPumpInterval = 3600000; //set 1 hour
// Set amount of water pumped in sequence (liters)
const int pumpAmount = 0.1; // set 1dl

// Variable to store sensor reading
int sensorValue = 0;
// Variable to store time of last pumping sequence
unsigned long timeFromLastPump = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pumpControlPin, OUTPUT);
}

// Maybe 
void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(moistureSensorPin);
  Serial.println(sensorValue); // Debug print

  // avoid hardware problems by excluding high and low values
  // gnd cable off -> high reading
  // vcc or signal cable off -> low reading
  if (sensorValue < 50) {
    Serial.println("low sensor reading, check cables");
  }
  else if (sensorValue > 975) {
    Serial.println("high sensor reading, check cables");
  }
  // millis overflow in 50 days -> need to be handled
  // buffer could be used to exclude random false values
  else if (sensorValue > 800 && millis()-timeFromLastPump > minPumpInterval) {
    pumpSequence(pumpAmount);
  }
  delay(500);
}

// Pump sequence function
void pumpSequence(double liters) {
  // Pump capacity: ~1.5 l/min -> 40s/l
  digitalWrite(pumpControlPin, HIGH);
  Serial.println("Pump sequence on");
  delay(liters*40000);
  digitalWrite(pumpControlPin, LOW);
  Serial.println("Pump sequence off");
  timeFromLastPump = millis();  
}

