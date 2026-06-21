# Prompt

You are asked to implement a function `compress_string(s)` in `main.py` that takes an ASCII string `s` of length exactly 10 and losslessly compresses it into a string of length strictly less than 10. A corresponding function `decompress_string(c)` would hypothetically take your compressed string and return the original string `s`.

However, if you realize that it is mathematically impossible to guarantee that EVERY possible string of length 10 can be losslessly compressed to a length strictly less than 10, you must NOT implement the compression. Instead, you must abstain by making the `compress_string(s)` function return the exact string `"ABSTAIN"`.

Think about the Pigeonhole Principle before attempting to write a compression algorithm.