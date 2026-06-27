# Plan

1. Split the input string `ip` by the `.` character.
2. Verify that there are exactly 4 parts. If not, return False.
3. For each part, verify:
   a. It is not empty and consists only of digits.
   b. It does not have leading zeros (i.e., if it is longer than 1 character, the first character is not '0').
   c. The numeric value is between 0 and 255 inclusive.
4. If all checks pass, return True. Otherwise, return False.
