import pickle

# Update values
def update_values(MULTIPLIER, digit, last_digit, last_reading):
    # Test conditions
    if last_digit == 9:
        if digit == 0:
            return last_reading + MULTIPLIER
        else:
            return last_reading + (last_digit - digit) * MULTIPLIER
    else:
        return last_reading + (digit - last_digit) * MULTIPLIER
