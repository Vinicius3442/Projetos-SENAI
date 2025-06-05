//Vinicius A. L. Montuani, Pietro
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(6, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
}

void loop()
{
  if(digitalRead(6) == LOW) {
    digitalWrite(2, HIGH);
  }
  
  else if (digitalRead(5) == LOW) {
    digitalWrite (2, LOW);
    
  }
}
