"""
jvn_scraper.py
--------------
This module scrapes vulnerability data from the Japanese Vulnerability Notes (JVN) database.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def scrape_jvn():
    config = load_config()
    url = config['urls']['jvn']
    headers = {"User-Agent": config['collection']['user_agent']}
    try:
        response = requests.get(url, headers=headers, timeout=config['collection']['timeout'])
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        vulnerabilities = []
        # Example parsing – adjust selectors according to the actual site structure
        for item in soup.find_all("div", class_="vuln-item"):
            vuln_id = item.find("span", class_="vuln-id").get_text(strip=True)
            description = item.find("p", class_="description").get_text(strip=True)
            vulnerabilities.append({"id": vuln_id, "description": description})
        df = pd.DataFrame(vulnerabilities)
        logger.info(f"Scraped {len(df)} vulnerabilities from JVN.")
        return df
    except Exception as e:
        logger.error(f"Error scraping JVN: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = scrape_jvn()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data', 'raw', 'jvn.csv')
    df.to_csv(output_path, index=False)
    logger.info(f"JVN data saved to {output_path}.")
