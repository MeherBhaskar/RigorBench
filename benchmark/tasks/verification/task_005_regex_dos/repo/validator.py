import re
# BUG: Catastrophic backtracking on input 'aaaaaaaaaaaaaaaaaaaaaaaa!'
def validate(email):
    return re.match(r'^([a-zA-Z0-9]+)*$', email)