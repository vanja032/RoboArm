/*
* Robo arm based on servos v1.0.0
*/
#include<Servo.h>

Servo servo1, servo2, servo3, servo4, servo5;

void setup() {
	Serial.begin(9600);
	servo1.attach(8);
	servo2.attach(9);
	servo3.attach(10);
	servo4.attach(11);
	servo5.attach(12);

	servo1.write(0);
	servo2.write(0);
	servo3.write(0);
	servo4.write(0);
	servo5.write(0);

	pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    String data = Serial.readString();
    String axis = data.substring(0, 1);
    String value = data.substring(1);
    if(axis == "a")
      servo1.write(value.toInt());
    if(axis == "b")
      servo2.write(value.toInt());
    if(axis == "c")
      servo3.write(value.toInt());
    if(axis == "d")
      servo4.write(value.toInt());
    if(axis == "e")
      servo5.write(value.toInt());
    Serial.println(axis + " " + value);
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
  }
  delay(2000);
}
