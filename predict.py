from model_training import train_model
import numpy as np

model = train_model()

today_price = float(input("Enter today’s closing price: "))
sentiment = float(input("Enter today’s sentiment score: "))

prediction = model.predict(np.array([[today_price, sentiment]]))
print("Predicted next day price:", prediction[0])
