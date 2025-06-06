#include <DHT.h>
#include <Servo.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const int ledVerde = 3;
const int ledAmarelo = 4;
const int ledVermelho = 5;
const int buzzer = 6;

Servo servo;
const int servoPin = 7;
const int buttonPin = 8;

bool overrideManual = false;
bool lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

float temperatura = 0;
String estado = "Normal";
String modo = "Auto";

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  servo.attach(servoPin);
  servo.write(0);

  Serial.println("Sistema iniciado.");
}

void loop() {
  bool reading = digitalRead(buttonPin);
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading == LOW && lastButtonState == HIGH) {
      overrideManual = !overrideManual;
      modo = overrideManual ? "Manual" : "Auto";
    }
  }

  lastButtonState = reading;
  temperatura = dht.readTemperature();

  if (isnan(temperatura)) {
    Serial.println("Erro ao ler DHT11");
    return;
  }

  if (!overrideManual) {
    if (temperatura < 25) {
      setEstado("Normal");
    } else if (temperatura < 30) {
      setEstado("Atenção");
    } else {
      setEstado("Perigo");
    }
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" °C | Estado: ");
  Serial.print(estado);
  Serial.print(" | Modo: ");
  Serial.println(modo);

  delay(1000);
}

void setEstado(String novoEstado) {
  estado = novoEstado;
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, LOW);
  digitalWrite(buzzer, LOW);
  servo.write(0);

  if (estado == "Normal") {
    digitalWrite(ledVerde, HIGH);
  } else if (estado == "Atenção") {
    digitalWrite(ledAmarelo, HIGH);
  } else if (estado == "Perigo") {
    digitalWrite(ledVermelho, HIGH);
    digitalWrite(buzzer, HIGH);
    servo.write(90);
  }
}
A