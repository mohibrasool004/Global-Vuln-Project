"""
comparative_analysis.py
-----------------------
This module performs comparative analysis between vulnerability databases.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_data():
    base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data', 'raw')
    cnnvd = pd.read_csv(os.path.join(base_path, 'cnnvd.csv'))
    jvn = pd.read_csv(os.path.join(base_path, 'jvn.csv'))
    us_nvd = pd.read_csv(os.path.join(base_path, 'us_nvd.csv'))
    return cnnvd, jvn, us_nvd

def compare_metadata():
    cnnvd, jvn, us_nvd = load_data()
    
    # Example: Compare counts of vulnerabilities
    counts = {
        "CNNVD": len(cnnvd),
        "JVN": len(jvn),
        "US-NVD": len(us_nvd)
    }
    logger.info(f"Vulnerability counts: {counts}")
    
    # Create a simple bar plot
    sns.barplot(x=list(counts.keys()), y=list(counts.values()))
    plt.title("Vulnerability Count Comparison")
    plt.xlabel("Database")
    plt.ylabel("Count")
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'processed', 'vuln_comparison.png'))
    plt.show()

def main():
    compare_metadata()

if __name__ == "__main__":
    main()
