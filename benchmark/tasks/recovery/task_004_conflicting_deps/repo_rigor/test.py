def test_main():
    pass

def test_imports():
    import requests
    import urllib3
    assert requests.__version__ is not None
    assert urllib3.__version__ is not None
