/*
**
** References :
** https://www.tutorialspoint.com/arduino/arduino_ultrasonic_sensor.htm
**
*/
 
const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
const int ledPin =  4;// the number of the LED pin

// Variables will change:
int ledState = LOW;             // ledState used to set the LED

void setup() {
   Serial.begin(9600); // Starting Serial Terminal
   // set the digital pin as output:
   pinMode(ledPin, OUTPUT);
}

void loop() {
   long duration, inches, cm;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   inches = microsecondsToInches(duration);
   cm = microsecondsToCentimeters(duration);
   Serial.print(inches);
   Serial.print("in, ");
   Serial.print(cm);
   Serial.print("cm");
   Serial.println();
   if(cm < 30 ) {
    digitalWrite(ledPin, HIGH);
   }
   else {
    digitalWrite(ledPin, LOW);
   }
   delay(50);
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
