from main import first_non_repeating_char

def test_first_non_repeating_char():
    assert first_non_repeating_char("leetcode") == "l"
    assert first_non_repeating_char("loveleetcode") == "v"
    assert first_non_repeating_char("aabb") is None
    assert first_non_repeating_char("") is None
