import pytest
from main import reverse_preserve_spaces

def test_reverse_preserve_spaces():
    assert reverse_preserve_spaces("hello world") == "dlrow olleh"
    assert reverse_preserve_spaces("a b c") == "c b a"
    assert reverse_preserve_spaces("  abc  ") == "  cba  "
    assert reverse_preserve_spaces("no_spaces") == "secaps_on"
    assert reverse_preserve_spaces("") == ""
    assert reverse_preserve_spaces("   ") == "   "
