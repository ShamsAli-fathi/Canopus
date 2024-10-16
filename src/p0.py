import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('mod.csv')

# Sample data (replace with your actual data)
x = data['distance'].to_numpy()
y = data['signal'].to_numpy()

# Create polynomial features object
poly = PolynomialFeatures(degree=3)

# Transform the features to include polynomial terms
x_poly = poly.fit_transform(x.reshape(-1, 1))

# Create and train the linear regression model
model = LinearRegression()
model.fit(x_poly, y)

# Predict the output for input 10
x_new = np.array([10])
x_new_poly = poly.transform(x_new.reshape(-1, 1))
y_predicted = model.predict(x_new_poly)

# Print the predicted output
print("Predicted output for input 10 (x = 10):", y_predicted[0])

x_plot = np.linspace(min(x), max(x), 100)  # 100 points between min and max of x
x_plot_poly = poly.transform(x_plot.reshape(-1, 1))
y_plot = model.predict(x_plot_poly)

# Plot the data and the fitted curve
plt.scatter(x, y, label='Data')
plt.plot(x_plot, y_plot, label='Fitted Curve')
plt.xlabel('Distance')
plt.ylabel('Signal')
plt.title('Polynomial Regression')
plt.legend()
plt.grid(True)
plt.show()
