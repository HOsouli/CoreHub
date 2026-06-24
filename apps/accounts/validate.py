import re

def mobile_validate(value):
    value = str(value).strip()
    pattern = r"^09\d{9}$"
    if not re.match(pattern, value):
        raise ValueError("شماره موبایل معتبر نیست. مثال: 09123456789")
    return value
