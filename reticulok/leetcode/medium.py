def int_to_roman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.
    This method is only expected to work for values between
    1 and 3999.
    
    Args:
        num (int): integer value to be converted to Roman numeral
    
    Returns:
        str: Roman numeral representation of integer
    """
    if not 1 <= num <= 3999:
        raise ValueError("number not between 1 and 3999 (%s)", num)

    numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    def find_next_numeral(rem: int) -> dict:
        for key in numerals:
            if rem - numerals[key] >= 0:
                return key, numerals[key]

    res = []
    rem = num
    while rem > 0:
        next_numeral, next_int = find_next_numeral(rem)
        res.append(next_numeral)
        rem -= next_int

    return "".join(res)
