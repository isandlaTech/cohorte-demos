
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:
  String input = "";
  while(Serial.available() > 0)
  {
    input += (char) Serial.read();
    delay(5);
  }
  if (input == "on")
  {
    digitalWrite(led, HIGH);
  }
  else if (input == "off")
  {
    digitalWrite(led, LOW);
  }
}
