import serial
import pandas as pd
from datetime import datetime

ser = serial.Serial('COM3', 9600)
data = []

print("Collecting data... Press Ctrl+C to stop")

try:
    while True:
        line = ser.readline().decode().strip()
        soil, gas = map(int, line.split(','))
        soil_moisture = 1023 - soil
        label = 1 if soil_moisture < 300 else 0  # 1 = irrigation needed

        data.append([soil, gas, label])
        print(soil, gas, label)

except KeyboardInterrupt:
    df = pd.DataFrame(data, columns=["soil", "gas", "irrigation_needed"])
    df.to_csv("sensor_data.csv", index=False)
    print("Dataset saved!")
