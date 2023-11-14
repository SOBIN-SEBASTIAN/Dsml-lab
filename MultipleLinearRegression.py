import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv('score.csv')
x = data['Hours'].values
y = data['Scores'].values
model = LinearRegression()
model.fit(x.reshape(-1,1), y)
y_pred = model.predict(x.reshape(-1,1))
new_study_hours = int(input("Enter the Study hours: "))
predicted_score = model.predict(np.array([new_study_hours]).reshape(-1, 1))
print(f" Exam Score : {predicted_score[0]}")
slope = model.coef_[0]
intercept = model.intercept_
print("Slope (Coefficient):", slope)
print("Y-Intercept:", intercept)
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.title('Linear Regression')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()