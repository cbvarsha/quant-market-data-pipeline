from src.app import validate_prices, historical_var
def test_quality_gate(): assert validate_prices([{"open":10,"high":9,"low":8,"close":10}])
def test_var_nonnegative(): assert historical_var([100,101,99,102,98])>=0
