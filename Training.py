import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("sensor_data.csv")

X = df[["soil", "gas"]]
y = df["irrigation_needed"]

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

joblib.dump(model, "soil_model.pkl")
print("Model trained & saved")
