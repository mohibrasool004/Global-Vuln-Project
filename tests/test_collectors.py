import os
import pandas as pd
from src.collectors import cnnvd_scraper, jvn_scraper, us_nvd_collector

def test_cnnvd_scraper():
    df = cnnvd_scraper.scrape_cnnvd()
    assert isinstance(df, pd.DataFrame)
    # Adjust conditions based on expected data

def test_jvn_scraper():
    df = jvn_scraper.scrape_jvn()
    assert isinstance(df, pd.DataFrame)

def test_us_nvd_collector():
    df = us_nvd_collector.fetch_us_nvd()
    assert isinstance(df, pd.DataFrame)
