//Vinicius Montuani N°29, Davi N°5, Vitor Gaspar N°31, Maria N°19
int trig = 4;
int echo = 5;
int buzzer = 2;
float centimetro;
long leitor;
void setup() {

  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(8, OUTPUT);

}
 
void loop() {

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  leitor = pulseIn(echo, HIGH);
  centimetro = (leitor / 2.0) / 29.1;
  Serial.print("Distância em cm: ");
  Serial.println(centimetro);

  if (centimetro < 100) {

    int intervalo = map(centimetro, 0, 100, 100, 1000);
 
    tone(buzzer, 1000);
    digitalWrite(8, HIGH);
    delay(100);
    noTone(buzzer);
    digitalWrite(8, LOW);
    delay(intervalo - 100);

  } else {

    noTone(buzzer);
    digitalWrite(8, LOW);
    delay(200);

  }

}

 