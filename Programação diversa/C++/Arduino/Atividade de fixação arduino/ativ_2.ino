//Vinicius Montuani N°29, Davi N°5, Vitor Gaspar N°31, Maria N°19
const int buzzerPin = 9;
const int buttonPin = 7;
bool buzzerState = false;
bool lastButtonState = HIGH;
bool currentButtonState;
 
void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(buzzerPin, LOW);
}
 
void loop() {
  currentButtonState = digitalRead(buttonPin);
 

  if (lastButtonState == HIGH && currentButtonState == LOW) {
    buzzerState = !buzzerState;
    digitalWrite(buzzerPin, buzzerState ? HIGH : LOW);
    delay(200);
  }
 
  lastButtonState = currentButtonState;
}