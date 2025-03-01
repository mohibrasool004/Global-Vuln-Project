"""
us_nvd_collector.py
-------------------
This module retrieves vulnerability data from the US National Vulnerability Database (US-NVD) via its REST API.
"""

import requests
import pandas as pd
import yaml
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def fetch_us_nvd():
    config = load_config()
    base_url = config['urls']['us_nvd']
    headers = {"User-Agent": config['collection']['user_agent']}
    params = {
        "resultsPerPage": 1000,  # adjust as needed
        "startIndex": 0
    }
    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=config['collection']['timeout'])
        response.raise_for_status()
        data = response.json()
        vulnerabilities = []
        # Parse the JSON structure (example – adjust keys as per the API response)
        for item in data.get("result", {}).get("CVE_Items", []):
            vuln_id = item.get("cve", {}).get("CVE_data_meta", {}).get("ID")
            description_data = item.get("cve", {}).get("description", {}).get("description_data", [])
            description = description_data[0]["value"] if description_data else ""
            vulnerabilities.append({"id": vuln_id, "description": description})
        df = pd.DataFrame(vulnerabilities)
        logger.info(f"Fetched {len(df)} vulnerabilities from US-NVD.")
        return df
    except Exception as e:
        logger.error(f"Error fetching US-NVD data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_us_nvd()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data', 'raw', 'us_nvd.csv')
    df.to_csv(output_path, index=False)
    logger.info(f"US-NVD data saved to {output_path}.")
