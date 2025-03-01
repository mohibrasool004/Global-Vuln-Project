"""
correlation_engine.py
---------------------
This module implements cross-database vulnerability matching.
"""

import os
import pandas as pd
from fuzzywuzzy import fuzz
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_all_data():
    base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data', 'raw')
    cnnvd = pd.read_csv(os.path.join(base_path, 'cnnvd.csv'))
    jvn = pd.read_csv(os.path.join(base_path, 'jvn.csv'))
    us_nvd = pd.read_csv(os.path.join(base_path, 'us_nvd.csv'))
    return cnnvd, jvn, us_nvd

def match_vulnerabilities(df1, df2, threshold=80):
    """
    For each vulnerability in df1, try to find a matching entry in df2 based on description similarity.
    """
    matches = []
    for idx1, row1 in df1.iterrows():
        for idx2, row2 in df2.iterrows():
            score = fuzz.token_set_ratio(row1['description'], row2['description'])
            if score >= threshold:
                matches.append({
                    "df1_id": row1['id'],
                    "df2_id": row2['id'],
                    "score": score
                })
    return pd.DataFrame(matches)

def run_correlation():
    cnnvd, jvn, us_nvd = load_all_data()
    logger.info("Matching CNNVD and JVN vulnerabilities.")
    matches_cnnvd_jvn = match_vulnerabilities(cnnvd, jvn)
    logger.info(f"Found {len(matches_cnnvd_jvn)} matches between CNNVD and JVN.")
    
    logger.info("Matching US-NVD and CNNVD vulnerabilities.")
    matches_us_cnnvd = match_vulnerabilities(us_nvd, cnnvd)
    logger.info(f"Found {len(matches_us_cnnvd)} matches between US-NVD and CNNVD.")
    
    # Save matches for further review
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data', 'processed', 'vuln_matches.csv')
    combined_matches = pd.concat([matches_cnnvd_jvn, matches_us_cnnvd], ignore_index=True)
    combined_matches.to_csv(output_path, index=False)
    logger.info(f"Correlation results saved to {output_path}.")

if __name__ == "__main__":
    run_correlation()
