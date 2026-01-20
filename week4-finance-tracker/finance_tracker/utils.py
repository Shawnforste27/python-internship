def valid_amount(amount):
    try:
        return float(amount) > 0
    except ValueError:
        return False
