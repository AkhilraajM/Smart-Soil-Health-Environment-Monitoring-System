import serial
import joblib
import pandas as pd

ser = serial.Serial('COM3', 9600)
model = joblib.load("soil_model.pkl")

while True:
    line = ser.readline().decode().strip()
    soil, gas = map(int, line.split(','))

    X_live = pd.DataFrame([[soil, gas]], columns=["soil", "gas"])
    prediction = model.predict(X_live)[0]

    if prediction == 1:
        ser.write(b"WATER_ON\n")
        print("Irrigation ON")
    else:
        ser.write(b"WATER_OFF\n")
        print("Irrigation OFF")

    # Simple anomaly check
    if gas > 600:
        ser.write(b"GAS_ALERT\n")
