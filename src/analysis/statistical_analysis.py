"""
statistical_analysis.py
-----------------------
This module implements statistical analyses such as PCA and ARIMA modeling.
"""

import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from src.utils.logger import get_logger

logger = get_logger(__name__)

def perform_pca(data, n_components=3):
    # Assume `data` is a DataFrame of numerical features for vulnerabilities
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data)
    logger.info(f"PCA explained variance ratios: {pca.explained_variance_ratio_}")
    return principal_components

def perform_arima(time_series, order=(1,1,1)):
    # Fit ARIMA model for time series data (e.g., counts per day)
    model = ARIMA(time_series, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    logger.info("ARIMA forecasting complete.")
    return model_fit, forecast

def main():
    # Example: perform PCA on random numerical data (replace with real vulnerability features)
    dummy_data = pd.DataFrame(np.random.rand(100, 5), columns=[f"feature_{i}" for i in range(5)])
    pcs = perform_pca(dummy_data, n_components=3)
    
    # Example: ARIMA on a dummy time series
    date_range = pd.date_range(start="2023-01-01", periods=100, freq='D')
    time_series = pd.Series(np.random.rand(100), index=date_range)
    model_fit, forecast = perform_arima(time_series)
    
    # Plot the ARIMA forecast
    plt.figure(figsize=(10, 5))
    plt.plot(time_series, label="Original")
    plt.plot(forecast.index, forecast, label="Forecast", color='red')
    plt.legend()
    plt.title("ARIMA Forecast")
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'processed', 'arima_forecast.png'))
    plt.show()

if __name__ == "__main__":
    main()
