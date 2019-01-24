String incoming = "";
const int Rpin = 9;
const int Gpin = 10;
const int Bpin = 11;


void setup() {
  // put your setup code here, to run once:
  pinMode(Rpin, OUTPUT);
  pinMode(Gpin, OUTPUT);
  pinMode(Bpin, OUTPUT);

  // opens serial port, sets data rate to 9600 bps
  Serial.begin(115200); 
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    // read the incoming:
    incoming = Serial.readString();
    // say what you got:
    //Serial.println(incoming); 
    
    //Serial.println(incoming[0]); 
    //Serial.println(incoming[1]); 
    //Serial.println(incoming[2]); 

    //analogWrite(Rpin,(incoming[0]- 48)*255/10 );
    //analogWrite(Gpin,(incoming[1]- 48)*255/10 );
    //analogWrite(Bpin,(incoming[2]- 48)*255/10 );

    analogWrite(Rpin,incoming[0]);
    analogWrite(Gpin,incoming[1]);
    analogWrite(Bpin,incoming[2]);

      
  }
}
