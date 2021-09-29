#include <Servo.h>
Servo s;

String x;
void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 s.attach(6);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString();
 if(x=="1"){
  s.write(90);
  delay(5000);
  //x = "4567";
  }
  s.write(0);
}
