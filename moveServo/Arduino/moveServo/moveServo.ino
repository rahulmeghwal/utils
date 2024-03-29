/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int defpos = 140;
int maxpos = 250;
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
//myservo.write(90);              // tell servo to go to position in variable 'pos'
  /*
  for (pos = defpos; pos <= maxpos ; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1);                       // waits 15ms for the servo to reach the position
  }
  delay(1000);
  for (pos = maxpos ; pos >= defpos; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1);                       // waits 15ms for the servo to reach the position
  }
  */
  myservo.write(45);              // tell servo to go to position in variable 'pos'
  delay(1000);
  myservo.write(145);              // tell servo to go to position in variable 'pos'
  delay(1000);
}
