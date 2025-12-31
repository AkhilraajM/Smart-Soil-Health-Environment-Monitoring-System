# Smart Soil Health & Environment Monitoring System

This project demonstrates an **end-to-end Arduino, Python, and Machine Learning–based system** for monitoring soil moisture and environmental gas levels, with automated irrigation control. It is designed to showcase practical skills in **embedded systems, serial communication, and applied ML**.

## Folder Structure

```
SoilHealthandEnvironmentMoniteringSystem/
├── DataCollection.py                  # Script for gathering sensor data
├── Interface.py                       # Live monitoring and ML execution script
├── Training.py                        # ML Model training script
├── SoilHealthandEnvironmentMoniteringSystem.ino  # Arduino Firmware
├── soil_model.pkl                     # Trained ML model file
├── sensor_data.csv                    # Dataset for training
└── README.md                          # Project documentation
```

## Project Overview

The system continuously monitors environmental health through:

- **Soil Moisture**: Measured via an analog soil moisture sensor
- **Gas Concentration**: Monitored via an MQ-series gas sensor

### How it Works

1. **Arduino UNO** reads raw analog data and transmits it to a Python application via Serial Communication
2. **Python** processes the data and uses a Decision Tree Machine Learning model to determine if irrigation is required
3. **Command Feedback**: Python sends a command back to the Arduino to toggle the Water Pump (Motor) and Buzzer based on the prediction

## 🛠 Hardware & Software Requirements

### Hardware

- Arduino UNO
- Soil Moisture Sensor (Analog)
- MQ Gas Sensor (Analog)
- DC Motor / Water Pump
- Relay Module or Motor Driver
- Buzzer
- Jumper wires, Breadboard, and USB Cable

### Software

- **OS**: Windows 10/11
- **IDE**: Arduino IDE
- **Language**: Python 3.7+
- **Libraries**: `pyserial`, `numpy`, `pandas`, `scikit-learn`

## Installation & Setup

### 1. Arduino Setup

1. Connect your Arduino UNO to your PC
2. Open `SoilHealthandEnvironmentMoniteringSystem.ino` in the Arduino IDE
3. Select the correct Board and COM Port
4. Upload the sketch

> **Important**: Close the Serial Monitor after uploading to allow Python to access the port.

### 2. Python Environment Setup

Navigate to your project directory and install dependencies:

```bash
pip install pyserial numpy pandas scikit-learn
```

## Workflow

### Step 1: Data Collection

Run the collection script to gather real-time sensor readings:

```bash
python DataCollection.py
```

- Data is saved to `sensor_data.csv`
- Ensure the Arduino is connected and the port matches the code

### Step 2: Model Training

Train the Machine Learning model using the collected data:

```bash
python Training.py
```

- This generates `soil_model.pkl`
- It utilizes a Decision Tree classifier to learn the threshold between "Dry" and "Wet" states

### Step 3: Live System Execution

Start the real-time monitoring and automated control system:

```bash
python Interface.py
```

## Technical Specifications

### Serial Data Format

The Arduino transmits data as a comma-separated string:

```
soil_value,gas_value
```

Example: `1002,224`

### Sensor Reading Range & Interpretation

| Sensor | Range | Interpretation |
|--------|-------|----------------|
| Soil Moisture | 0 - 1023 | Higher value = Drier Soil |
| Gas Sensor | 0 - 1023 | Higher value = Higher Concentration |

### Irrigation Logic

- **Prediction: ON** → Motor Activates (Dry Soil detected by ML)
- **Prediction: OFF** → Motor Deactivates (Sufficient moisture)

## Troubleshooting

- **COM Port Access Denied**: Ensure the Arduino Serial Monitor is closed before running Python scripts
- **Inverted Logic**: Soil sensors often return higher values for dry soil; the code includes calibration to handle this inversion
- **Feature Warning**: If you see a "Missing Feature Names" warning during prediction, it is a known scikit-learn behavior that does not impact prediction accuracy

## Future Improvements

- Integrate DHT11/22 for Temperature and Humidity
- Add a Web Dashboard for remote data visualization
- Implement IoT capabilities (ESP8266/ESP32) for cloud storage
- Deploy a deep learning model for more complex environmental predictions

## Author

**Akhilraaj M**  
Embedded Systems | Computer Vision | Applied Machine Learning

## License


This project is open source and available for educational purposes.
