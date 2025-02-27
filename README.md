# Global Vulnerability Database Research: Cross Reference and Analysis Framework

This project creates an automated framework to collect, analyze, and correlate vulnerability data from multiple national databases: US-NVD, CNNVD, and JVN.

## Features
- **Automated Data Collection:** Scrapers and API integrators for CNNVD, JVN, and US-NVD.
- **Comparative Analysis:** Metadata mapping, coverage, and temporal analysis.
- **Correlation Engine:** Cross-database matching with confidence scoring.
- **Gap Analysis:** Identification of coverage gaps for US critical infrastructure.
- **Statistical Analysis:** Multivariate and time series models (e.g., PCA, ARIMA) for vulnerability trends.
- **Data Quality & Validation:** Outlier detection, missing data imputation, and more.

## Project Structure
Refer to the directory tree in the documentation for file and folder details.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://your-repo-url.git
   cd GlobalVulnProject
2. Create a Virtual Environment and Install Dependencies:
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
3.Configure the Project: Update config/config.yaml with API endpoints and other settings as needed.
4.Run the Project:

To run collectors:
bash
Copy code
python -m src.collectors.cnnvd_scraper
python -m src.collectors.jvn_scraper
python -m src.collectors.us_nvd_collector
To perform analysis:
bash
Copy code
python -m src.analysis.comparative_analysis
python -m src.analysis.statistical_analysis
To run correlation engine and gap analysis:
bash
Copy code
python -m src.correlation.correlation_engine
python -m src.gap_analysis.gap_analysis"# Global-Vuln-Project" 
