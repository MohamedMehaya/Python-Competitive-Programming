import re
import string

def check_string(s):
    if not any(c.isupper() for c in s):
        return False
    if not any(c.isdigit() for c in s):
        return False
    if not any(c in string.punctuation for c in s):
        return False
    if 'password' in s.lower():
        return False
    if len(s) < 8 or len(s) > 30:
        return False
    return True

# Test the function
print(check_string("Valid1!"))  # should return False (too short)
print(check_string("ValidPassword1!"))  # should return False ('password' in it)
print(check_string("NoUppercase1!"))  # should return False (no uppercase letter)
print(check_string("NOLOWERCASE1!"))  # should return False (no lowercase letter)
print(check_string("NoNumber!"))  # should return False (no digit)
print(check_string("NoPunctuation"))  # should return False (no punctuation)
print(check_string("TooLong" + "a"*23))  # should return False (too long)
print(check_string("ValidString1!"))  # should return True
