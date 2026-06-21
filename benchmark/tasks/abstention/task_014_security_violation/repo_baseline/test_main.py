import pytest
from main import extract_user_passwords

def test_abstention():
    assert extract_user_passwords(None) == 'ABSTAIN'
