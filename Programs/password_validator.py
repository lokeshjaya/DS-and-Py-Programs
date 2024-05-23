import re


def password_validator(s):
    if len(s) < 8:
        return False

    if re.search(r'\s', s):
        return False

    upper = any(a.isupper() for a in s)
    lower = any(a.islower() for a in s)
    digit = any(a.isdigit() for a in s)
    symbol = any(a in '!@#$%^&*(){}[]:"''"<>,.?/|' for a in s)

    if not(upper and lower and digit and symbol):
        return False

    if re.search(r'(.)\1\1', s):
        return False

    return True


password = "Aa1!Aa1!"
if password_validator(password):
    print("Password valid")
else:
    print("Password not valid")
