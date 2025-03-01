"""
data_validation.py
------------------
Provides functions for data validation and quality assurance.
"""

import pandas as pd
import numpy as np
from scipy.stats import kstest
from src.utils.logger import get_logger

logger = get_logger(__name__)

def validate_distribution(data, dist='norm'):
    # Kolmogorov-Smirnov test for normality as an example.
    statistic, p_value = kstest(data, dist)
    logger.info(f"K-S test statistic: {statistic}, p-value: {p_value}")
    return statistic, p_value

def detect_missing_data(df):
    missing = df.isnull().sum()
    logger.info(f"Missing data per column:\n{missing}")
    return missing

def detect_outliers(df, feature):
    # Simple outlier detection using z-score
    mean_val = df[feature].mean()
    std_val = df[feature].std()
    threshold = 3
    df['z_score'] = (df[feature] - mean_val) / std_val
    outliers = df[abs(df['z_score']) > threshold]
    logger.info(f"Detected {len(outliers)} outliers in feature '{feature}'.")
    return outliers
