//Vinicius Montuani N°29, Davi N°5, Vitor Gaspar N°31, Maria N°19
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>
 
// Configuração do DHT11
#define DHTPIN 2
#define DHTTYPE DHT11
 
DHT dht(DHTPIN, DHTTYPE);
 
LiquidCrystal_I2C lcd(0x27, 16, 2);
 
void setup() {
  Serial.begin(9600);
  dht.begin();
 
  lcd.init();  
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Iniciando...");
  delay(2000);
  lcd.clear();
}
 
void loop() {
  float temp = dht.readTemperature();
 
  if (isnan(temp)) {
    lcd.setCursor(0, 0);
    lcd.print("Erro ao ler");
    lcd.setCursor(0, 1);
    lcd.print("sensor DHT11");0
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Temperatura:");
    lcd.setCursor(0, 1);
    lcd.print(temp);
    lcd.print(" C   ");
  }
 
  delay(2000);
}
 