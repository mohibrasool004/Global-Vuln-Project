import requests
import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Correct NVD API URL (v2.0)
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Optional: Add your API Key for better rate limits
API_KEY = "c76425c3-e1bb-4ad0-9ca6-5b3bc9c84f45"  # Replace with your key or leave empty

# ✅ Fix: Correct date format with 'Z' at the end (UTC time)
params = {
    "resultsPerPage": 1000,
    "startIndex": 0,
    "pubStartDate": "2024-01-01T00:00:00.000Z",
    "pubEndDate": "2024-02-28T23:59:59.999Z",
}

# ✅ Add API Key if available
if API_KEY:
    params["apiKey"] = API_KEY

def fetch_nvd_data():
    logger.info("Fetching CVE data from NVD...")
    response = requests.get(NVD_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("vulnerabilities", [])  # ✅ Correct key in v2.0
    else:
        logger.error(f"Error fetching data: {response.status_code} - {response.text}")
        return []

def save_to_csv(cve_list):
    if not cve_list:
        logger.warning("No data retrieved, CSV not created.")
        return

    extracted_data = []
    for item in cve_list:
        cve = item["cve"]
        cve_id = cve["id"]
        description = cve["descriptions"][0]["value"]
        severity = cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity", "N/A")

        extracted_data.append([cve_id, description, severity])

    df = pd.DataFrame(extracted_data, columns=["CVE_ID", "Description", "Severity"])
    
    # Save to CSV
    output_path = os.path.join(os.path.dirname(__file__), "../../data/raw/nvd_vulnerabilities.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"Data saved to {output_path}")

if __name__ == "__main__":
    cve_data = fetch_nvd_data()
    save_to_csv(cve_data)
