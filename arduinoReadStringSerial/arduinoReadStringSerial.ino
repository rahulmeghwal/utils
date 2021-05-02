String incoming = "";
const int Rpin = 9;
const int Gpin = 10;
const int Bpin = 11;
int oldR = 0, oldG = 0, oldB = 0,newR,newG,newB;
const int steps = 30;
float StepR, StepG, StepB;

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

  //while(Serial.available())
  //  incoming = Serial.readString();
    
  if (Serial.available() > 0) {
    // read the incoming:
    incoming = Serial.readString();
    // say what you got:
    Serial.println("incoming"); 
    Serial.println(incoming[0]); 
    Serial.println(incoming[1]); 
    Serial.println(incoming[2]); 
    
    // Scalevalues to 0 to 255
     newR = (incoming[0]- 48)*255/9 ;        
     newG = (incoming[1]- 48)*255/9 ;        
     newB = (incoming[2]- 48)*255/9 ;        
     
    //Serial.println(incoming[0]); 
    //Serial.println(incoming[1]); 
    //Serial.println(incoming[2]); 
    if( oldR != newR || oldG != newG || oldB != newB ){

      Serial.println("Old Values"); 
      Serial.println(oldR); 
      Serial.println(oldG); 
      Serial.println(oldB); 

      Serial.println("New Values"); 
      Serial.println(newR); 
      Serial.println(newG); 
      Serial.println(newB); 
      
      StepR = ((newR - oldR) / steps);
      StepG = ((newG - oldG) / steps);
      StepB = ((newB - oldB) / steps);
      
      int i =0 ;
      while( i < (steps + 3) ){
        newR = min(max(0,(oldR + StepR*i)), 255);
        newG = min(max(0,(oldG + StepG*i)), 255);
        newB = min(max(0,(oldB + StepB*i)), 255);
        analogWrite(Rpin, newR);
        analogWrite(Gpin, newG);
        analogWrite(Bpin, newB );

        Serial.println( newR ); 
        //Serial.println(255 - (oldG + StepG*i)); 
        //Serial.println(255 - (oldB + StepB*i)); 

          
        delay(30);
        i++;
      }
    oldR = newR;
    oldG = newG;
    oldB = newB;

    while(Serial.available())
          Serial.read();

    delay(100);        
    }

    //analogWrite(Rpin,(incoming[0]- 48)*255/10 );
    //analogWrite(Gpin,(incoming[1]- 48)*255/10 );
    //analogWrite(Bpin,(incoming[2]- 48)*255/10 );
    
    //analogWrite(Rpin,incoming[0]);
    //analogWrite(Gpin,incoming[1]);
    //analogWrite(Bpin,incoming[2]);

      
  }
}
