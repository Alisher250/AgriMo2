#include <SoftwareSerial.h>
#include <Arduino.h>
#include <DHT.h>
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_Sensor.h>
#define DHTTYPE DHT22
#define BMP_SDA 21
#define BMP_SCL 22

Adafruit_BMP280 bmp280;
const int dhtPin = 32;
DHT dht(dhtPin, DHTTYPE);
const int flamePin = 13;
const int raindroapPin = 14;
const int lightPin = 27;
const int soilMoisturePin = 34;
const int ammoniaPin = 35;
unsigned long previousMillis = 0;

void setup() {
  Serial.begin(9600);
  Serial2.begin(9600);
  pinMode(flamePin, INPUT);  pinMode(raindropPin, INPUT);
 pinMode(lightPin, INPUT);
  pinMode(soilMoisturePin, INPUT);
  pinMode(ammoniaPin, INPUT);
  boolean status = bmp280.begin(0x76);
  dht.begin();
  delay(7000);
  test_sim800_module();
}
void loop() {
  updateSerial();
  unsigned long currentMillis = millis(); 
  if(currentMillis - previousMillis >= 500) {  
    send_SMS();  
    previousMillis = currentMillis;  
  }
}
void test_sim800_module()
{
  Serial2.println("AT");
  updateSerial();
  Serial.println();
  Serial2.println("AT+CSQ");
  updateSerial();
  Serial2.println("AT+CCID");
  updateSerial();
  Serial2.println("AT+CREG?");
  updateSerial();
  Serial2.println("ATI");
  updateSerial();
  Serial2.println("AT+CBC");
  updateSerial();
}
void updateSerial()
{
  delay(500);
  while (Serial.available())
  {
    Serial2.write(Serial.read());//Forward what Serial received to Software Serial Port
  }
  while (Serial2.available())
  {
    Serial.write(Serial2.read());//Forward what Software Serial received to Serial Port
  }
}
void send_SMS()
{
  float humidity = dht.readHumidity();
  float temperatureCelsius = dht.readTemperature();
  float temp = bmp280.readTemperature();
  float press = bmp280.readPressure() / 100;
  int rawValue = analogRead(raindropPin);

  if (isnan(humidity) || isnan(temperatureCelsius)) {
    Serial.println("Не удалось считать данные с датчика влажности и температуры воздуха(DHT)!");
    return;
  } 
  int flameValue = analogRead(flamePin);
  int flameValue1 = map(flameValue, 0, 4095, 1, 0);
  int rainValue = analogRead(raindropPin);
  int rainValue1 = map(rainValue, 2000, 4095, 100, 0);
  int lightValue = analogRead(lightPin);
  int lightValue1 = map(lightValue, 0, 4095, 100, 0);
  int soilMoistureValue = analogRead(soilMoisturePin);
  int soilMoistureValue1 = map(soilMoistureValue, 2330, 3300, 100, 0);
  int ammoniaValue = analogRead(ammoniaPin);
  String alerts = "";
  if(temperatureCelsius < 5) {
    alerts += "\nWarning: There is a risk of freezing!";
  }
  if(temperatureCelsius > 30 && soilMoistureValue1 < 30) {
    alerts += "\nWarning: Danger of drought!";
  }
  if(humidity > 80 && press < 980) {
    alerts += "\nWarning: Rain is possible!";
  }
  if (rainValue1 > 90) {
    alerts += "\nWarning:The risk of flooding has been detected!";
  }
  if (flameValue1 == 1) {
    alerts += "\nAttention: Fire detector!";
  }
  if(humidity > 80 && temperatureCelsius > 30 ) {
    alerts += "\nWarning: Risk of diseases due to high humidity and high temperature!";
  }
  if(lightValue1 > 90 && temperatureCelsius > 30) {
    alerts += "\nWarning: Strong solar radiation detected!";
  }
  if(ammoniaValue > 1000) {
    alerts += "\nWarning: High levels of ammonia, possible chemical spill!";
  }
  if (press > 1000) {
    alerts += "\nWarning: Low atmospheric pressure detected. Danger of storms!";
}

  Serial2.println("AT+CMGF=1");
  updateSerial();
  Serial2.println("AT+CMGS=\"+77718885212\"");
  updateSerial();
  Serial2.print("TEMP: " + String(temperatureCelsius) + " VLAGA: " + String(humidity) + " RAIN: " + String(rainValue1) + " RADIATION: " + String(lightValue1) + 
  " DAVLENIE: " + String(press) + " AMMONIA: " + String(ammoniaValue) + " FLAME: " + String(flameValue1) + " SOIL: " + String(soilMoistureValue1) + alerts);
  updateSerial();
  Serial.println();
  Serial.println("Message Sent");
  Serial2.write(26);
}