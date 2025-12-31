#define SOIL_PIN A0
#define GAS_PIN  A1
#define MOTOR_PIN 8
#define BUZZER_PIN 9
#define LED_PIN 13

void setup() {
  Serial.begin(9600);

  pinMode(MOTOR_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  digitalWrite(MOTOR_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  int soil = analogRead(SOIL_PIN);
  int gas  = analogRead(GAS_PIN);

  // Send data to Python
  Serial.print(soil);
  Serial.print(",");
  Serial.println(gas);

  // Listen for commands from Python
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "WATER_ON") {
      digitalWrite(MOTOR_PIN, HIGH);
      digitalWrite(LED_PIN, HIGH);
    }
    else if (cmd == "WATER_OFF") {
      digitalWrite(MOTOR_PIN, LOW);
      digitalWrite(LED_PIN, LOW);
    }
    else if (cmd == "GAS_ALERT") {
      tone(BUZZER_PIN, 1000, 500);
    }
  }

  delay(1000);
}
