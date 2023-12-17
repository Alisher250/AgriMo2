#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

const int servoMin = 150;
const int servoMax = 600;

// шаговый
const int stepPin = 11;
const int dirPin = 12;

const int RIGHT = 0;
const int LEFT = 1;

// шкив
int enA = 3;
int in1 = 5;
int in2 = 4;

// main variables
int donerightleft = 0;
int direction = 0; // 0 is for right // 1 us for left

bool lefttrue = false;
bool righttrue = false;
bool leftrightconfirmedtrue = false;

// sorting
int angle1height1sort = 0;
int angle2height1sort = 0;
int angle2height2sort = 0;
int angle1height2sort = 0;

int pos1sort = 0;
int pos2sort = 0;
int pos3sort = 0;
int pos4sort = 0;

int grabangle1sort = 0;
int angle1 = 0;
int angle2 = 0;
int turn_to = 90;


void setServoAngle(int servoNum, int angle) {
  if (angle < 0) {
    angle = 0;
  } else if (angle > 180) {
    angle = 180;
  }
  
  int pulseWidth = map(angle, 0, 180, servoMin, servoMax);
  
  pwm.setPWM(servoNum, 0, pulseWidth);
}

void setMultipleServoAngle(int angle1, int angle2) {
  int angle3;
  angle3 = (180 - (360 - (180 - angle1) - (180 - angle2) - 90) + 80);

  if (angle1 < 0) {
    angle1 = 0;
  } else if (angle1 > 180) {
    angle1 = 180;
  }
  if (angle2 < 0) {
    angle2 = 0;
  } else if (angle2 > 180) {
    angle2 = 180;
  }
  
  if (angle3 < 0) {
    angle3 = 0;
  } else if (angle3 > 180) {
    angle3 = 180;
  }

  int pulseWidth1 = map(angle1, 0, 180, servoMin, servoMax);
  int pulseWidth2 = map(angle2, 0, 180, servoMin, servoMax);
  int pulseWidth3 = map(angle3, 0, 180, servoMin, servoMax);
  
  pwm.setPWM(0, 0, pulseWidth1);
  pwm.setPWM(1, 0, pulseWidth2);
  pwm.setPWM(2, 0, pulseWidth3);
}

void setStartPosition() {
  int pulseWidth = map(0, 0, 180, servoMin, servoMax);
  int pulseWidth1 = map(180, 0, 180, servoMin, servoMax);
  int pulseWidth2 = map(90, 0, 180, servoMin, servoMax);
  int pulseWidth3 = map(90, 0, 180, servoMin, servoMax);
  int pulseWidth4 = map(80, 0, 180, servoMin, servoMax);
  pwm.setPWM(0, 0, pulseWidth);
  pwm.setPWM(1, 0, pulseWidth1);
  pwm.setPWM(2, 0, pulseWidth2);
  pwm.setPWM(3, 0, pulseWidth3);
  pwm.setPWM(4, 0, pulseWidth4);
}

void setServosPiston() {
  int pulseWidth = map(70, 0, 180, servoMin, servoMax);
  int pulseWidth1 = map(110, 0, 180, servoMin, servoMax);
  pwm.setPWM(5, 0, pulseWidth);
  pwm.setPWM(6, 0, pulseWidth1);
  delay(1000);
  int pulseWidth2 = map(0, 0, 180, servoMin, servoMax);
  int pulseWidth3 = map(180, 0, 180, servoMin, servoMax);
  pwm.setPWM(5, 0, pulseWidth2);
  pwm.setPWM(6, 0, pulseWidth3);
}

void rotateMotor(int angle, int direction) {
  int steps = (angle * 40 / 8 / 360.0) * 200;
  if (direction == 0) {
    digitalWrite(dirPin, HIGH);
  } else {
    digitalWrite(dirPin, LOW);
  }
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(4000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(4000);
  }
}

void moveServoWithSpeed(uint8_t servoNum, int targetAngle, int speed) {
  int currentAngle = map(pwm.getPWM(servoNum), servoMin, servoMax, 0, 180);
  while (currentAngle != targetAngle) {
    if (currentAngle < targetAngle) {
      currentAngle++;
    } else {
      currentAngle--;
    }
    setServoAngle(servoNum, currentAngle);
    delay(speed);
  }
}

void godown() {
  //ADILET WRITE HERE GRAB
  setMultipleServoAngle(90, 70);
  delay(1000);
  setMultipleServoAngle(120, 78);
  setServoAngle(4, 90);
  delay(1000);
  setMultipleServoAngle(140, 85);
  setServoAngle(4, 130);
  delay(1000);
  setServoAngle(4, 80);
  delay(1000);
  setServoAngle(1, 120);
  setServoAngle(0, 78);
  setServoAngle(2, 90);
  delay(1000);
  setStartPosition();
  delay(2000);
  rotateMotor(donerightleft, LEFT);
  setServoAngle(0, 90);
  setServoAngle(1, 90);
  delay(1000);
  setServoAngle(3, 180);
  delay(1000);
  setServoAngle(2, 180);
  delay(1000);
  setMultipleServoAngle(140, 30);
  delay(1000);
  setServoAngle(4, 120);
  delay(1000);
  setMultipleServoAngle(70, 90);
  delay(1000);
  setStartPosition();
  delay(1000);
  setServosPiston();
  Serial.println("saved");
}

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);

  // шаговый
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);

  // шкив
  pinMode(enA, OUTPUT);  
  pinMode(in1, OUTPUT);  
  pinMode(in2, OUTPUT);
  

  setStartPosition();
  delay(1000);

}



void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    
    if (command.startsWith("left ")) {
        if (!lefttrue) {
          lefttrue = true;
          direction = 1;
          rotateMotor(90, LEFT);
          donerightleft = 90;
          delay(3000);
          setMultipleServoAngle(90, 90);
          delay(1000);
          Serial.println("photorightleft");
        }
    } else if (command.startsWith("right ")) {
        if (!righttrue) {
          righttrue = true;
          rotateMotor(90, RIGHT);
          donerightleft = 90;
          delay(3000);
          setMultipleServoAngle(90, 90);
          delay(1000);
          Serial.println("photorightleft");
          direction = 0;
        }
    } else if (command.startsWith("Left-Right Confirmed ")) {
      if (!leftrightconfirmedtrue) {
        Serial.println("photoangle");
        delay(100);
        Serial.println("photoangle");
        delay(100);
        Serial.println("photoangle");
        leftrightconfirmedtrue = true;
      }
    } else if (command.startsWith("Step left for ")) {
      int steps = command.substring(14).toInt();
      donerightleft -= steps;
      rotateMotor(steps, LEFT);
      Serial.println("photorightleft");
    } else if (command.startsWith("Step right for ")) {
      int steps = command.substring(15).toInt();
      donerightleft += steps;
      rotateMotor(steps, RIGHT);
      Serial.println("photorightleft");
    } else if (command.startsWith("Turn grab right for ")) {
      int angle = command.substring(20).toInt();
      turn_to = (90 - angle);
      setServoAngle(3, turn_to);
      delay(1000);
      godown();
      delay(1000);
    } else if (command.startsWith("Turn grab left for ")) {
      int angle = command.substring(19).toInt();
      turn_to = (90 + angle);
      setServoAngle(3, turn_to);
      delay(1000);
      righttrue = false;
      leftrightconfirmedtrue = false;
      lefttrue = false;
      godown();
      delay(1000);
    }
  }


  // delay(500);

  // setServoAngle(4, 140);
  // delay(1000);
  // setServoAngle(4, 100);
  // delay(1000);


  // обратно в начальную позицию

  // setServoAngle(1, 180);

  // setServoAngle(3, 0);
  // delay(10000);
  // setServoAngle(0, 0);
  // // delay(500);

  // setServoAngle(2, 180);
  // delay(500);
  // setServoAngle(0, 90);
  // delay(500);

  // setServoAngle(2, 90);
  // delay(500);

  // шкиф
  // Up(2000);
  // delay(1000);
  // Down(1000);
  // delay(1000);

  // градус захвата
  // setServoAngle(0, 0);
  // delay(1000);
  // setServoAngle(2, 180);
  // delay(1000);
  // setServoAngle(0, 180);
  // delay(1000);

  //захват
  // setServoAngle(4, 38);
  // delay(1000);
  // setServoAngle(4, 14);
  // delay(1000);

  // setServoAngle(2, 0);
  // delay(1000);
  // setServoAngle(2, 180);
  // delay(1000);

  // шаговый
  // rotateMotor(90, LEFT);
  // delay(4000);
  // rotateMotor(90, RIGHT);
  // delay(2000);
}
