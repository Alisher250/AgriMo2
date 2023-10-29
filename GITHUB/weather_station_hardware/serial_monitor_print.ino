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
const int raindropPin = 14;
const int lightPin = 27;
const int soilMoisturePin = 34;
const int ammoniaPin = 35;
unsigned long previousMillis = 0;

void setup() {
  Serial.begin(9600);
  pinMode(flamePin, INPUT);
  pinMode(raindropPin, INPUT);
  pinMode(lightPin, INPUT);
  pinMode(soilMoisturePin, INPUT);
  pinMode(ammoniaPin, INPUT);
  boolean status = bmp280.begin(0x76);
  dht.begin();
  delay(7000);
}

void loop() {
  printSensorData();
  delay(60000);
}

void printSensorData() {
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
    alerts += "\nВнимание: Существует риск замораживания!";
}
if(temperatureCelsius > 30 && soilMoistureValue1 < 30) {
    alerts += "\nВнимание: Опасность засухи!";
}
if(humidity > 80 && press < 980) {
    alerts += "\nВнимание: Возможен дождь!";
}
if (rainValue1 > 90) {
    alerts += "\nВнимание: Обнаружен риск затопления!";
}
if (flameValue1 == 1) {
    alerts += "\nВнимание: Пожарный датчик!";
}
if(humidity > 80 && temperatureCelsius > 30 ) {
    alerts += "\nВнимание: Риск заболеваний из-за высокой влажности и высокой температуры!";
}
if(lightValue1 > 90 && temperatureCelsius > 30) {
    alerts += "\nВнимание: Обнаружено сильное солнечное излучение!";
}
if(ammoniaValue > 1000) {
    alerts += "\nВнимание: Высокий уровень аммиака, возможное химическое загрязнение!";
}
if (press > 1000) {
    alerts += "\nВнимание: Обнаружено низкое атмосферное давление. Опасность шторма!";
}

  // Output the data
  Serial.print("TEMPERATURA VOZDUHA: ");
  Serial.println(temperatureCelsius);
  Serial.print("VLAJNOST VOZDUHA: ");
  Serial.println(humidity);
  Serial.print("TEMPERATURA VOZDUHA 2: ");
  Serial.println(temp);
  Serial.print("DAVLENIE: ");
  Serial.println(press);
  Serial.print("VOSPLAMENENIE: ");
  Serial.println(flameValue1);
  Serial.print("DOJD: ");
  Serial.println(rainValue1);
  Serial.print("SVET: ");
  Serial.println(lightValue1);
  Serial.print("VLAJNOST POCHVY: ");
  Serial.println(soilMoistureValue1);
  Serial.print("AMMIAK: ");
  Serial.println(ammoniaValue);
  Serial.println(alerts);
  Serial.println("///////////////////////////////////////////////////////////////////////////////");
}
