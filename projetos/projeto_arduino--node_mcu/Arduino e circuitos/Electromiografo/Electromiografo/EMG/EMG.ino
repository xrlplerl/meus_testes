#include <Servo.h>

Servo myservo;
float sensorValue = 0;
int pos = 0;

void setup()
{
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop()
{
  sensorValue = analogRead(A0);
  pos = sensorValue / 6.5;
  myservo.write(pos);
  Serial.println(pos);
  delay(10);
}
