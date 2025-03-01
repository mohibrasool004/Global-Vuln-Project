import os
from src.analysis import comparative_analysis, statistical_analysis

def test_comparative_analysis():
    # This test runs the comparison function and checks if the plot file is created.
    comparative_analysis.compare_metadata()
    plot_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'vuln_comparison.png')
    assert os.path.exists(plot_path)

def test_statistical_analysis():
    # Run statistical analysis functions (ensure no exceptions occur)
    statistical_analysis.main()
