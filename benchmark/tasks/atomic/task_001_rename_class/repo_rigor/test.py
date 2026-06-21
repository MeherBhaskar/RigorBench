from core import NewManager
from api import m
from utils import check

def test_main():
    n = NewManager()
    n.start()
    assert isinstance(m, NewManager)
    assert isinstance(check(), NewManager)
