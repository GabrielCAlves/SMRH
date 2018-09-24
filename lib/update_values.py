# Update values
def update_values(MULTIPLIER, digit, last_digit, last_reading):
    # Test conditions
    if last_digit == digit:
        return last_reading;

    if last_digit == 9:
        if digit == 0:
            return last_reading + MULTIPLIER
        # else:
        return last_reading + (digit * MULTIPLIER) + MULTIPLIER

    if last_digit == 8:
        if digit == 0:
            return last_reading + 2 * MULTIPLIER

        if digit != 9:
            return last_reading + (digit * MULTIPLIER) + 2 * MULTIPLIER

    if last_digit > digit:
        return 'ERROR'

    # else:
    return last_reading + (digit - last_digit) * MULTIPLIER
