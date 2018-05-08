// Set IO pins
const int moistureSensorPin = A0;
const int pumpControlPin = 7;

// Set minimum interval between pumping sequences (milliseconds)
const long minPumpInterval = 3600000; //set 1 hour
// Set amount of water pumped in sequence (liters)
const int pumpAmount = 0.1; // set 1dl

// Variable to store sensor reading
int sensorValue = 0;
// Variable to store time of last pumping sequence
long timeFromLastPump = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pumpControlPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(moistureSensorPin);
  Serial.println(sensorValue); // Test print reading  
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

