from analysis import df
import pandas as pd

def test_main():
    assert len(df) == 4
    assert df.iloc[3, 0] == 4
