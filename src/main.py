import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def path_loss_model(distance, beta):
    P0 = -64  # Fixed
    return P0 - 10 * beta * np.log10(distance / d0)

# Import data
data = pd.read_csv('mod.csv')

# Sample data
measured_distance = data['distance']  
received_power = data['signal']

# Reference Distance
d0 = 10

bounds = ([-np.inf], [np.inf])

# Fit model
popt, pcov = curve_fit(path_loss_model, measured_distance, received_power, bounds=bounds)

beta_optimal = popt[0]

predicted_power = path_loss_model(measured_distance, beta_optimal)
residuals = received_power - predicted_power
sigma_optimal = np.std(residuals)

print("beta:", beta_optimal)
print("sigma:", sigma_optimal)
