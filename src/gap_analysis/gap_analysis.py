"""
gap_analysis.py
---------------
This module performs a gap analysis to identify coverage gaps in US critical infrastructure.
"""

import os
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_us_infrastructure():
    # For demonstration, load a CSV file listing critical US infrastructure products.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'raw', 'us_infrastructure.csv')
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded {len(df)} US infrastructure products.")
        return df
    except Exception as e:
        logger.error(f"Error loading US infrastructure data: {e}")
        return pd.DataFrame()

def load_us_nvd_data():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'raw', 'us_nvd.csv')
    return pd.read_csv(path)

def analyze_gap():
    infra_df = load_us_infrastructure()
    us_nvd_df = load_us_nvd_data()

    # Example: Identify products in the infrastructure list that do not appear in US-NVD vulnerability IDs.
    # (Assume both dataframes have a column 'product' for demonstration.)
    infra_products = set(infra_df['product'].str.lower().unique())
    nvd_products = set(us_nvd_df['description'].str.lower().unique())  # in reality, you'd extract product names from descriptions
    gap = infra_products.difference(nvd_products)
    
    logger.info(f"Identified {len(gap)} products with potential coverage gaps.")
    gap_df = pd.DataFrame({"product": list(gap)})
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'processed', 'coverage_gap.csv')
    gap_df.to_csv(output_path, index=False)
    logger.info(f"Gap analysis results saved to {output_path}.")

def main():
    analyze_gap()

if __name__ == "__main__":
    main()
