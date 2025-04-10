//Vinicius A. L. Montuani, Pietro
int ledPin = 9;
int potPin = A5;
int valorpot = 0;
int delayTime = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  valorpot = analogRead(potPin);
  delayTime = map(valorpot, 0, 1023, 50, 1000); 
  Serial.println(delayTime);
  
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin, LOW);
  delay(delayTime);
}