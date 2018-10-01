import shutil

f1 = PATH + '/server/static/images/last_picture.png'
f2 = PATH + '/server/static/images/source/last_picture.png'

# Update values
def update_values(PATH, MULTIPLIER, digit, last_digit, last_reading):
    # Test conditions
    if last_digit == digit:
        return last_reading

    if last_digit == 9:

        shutil.move(f1, f2)

        if digit == 0:
            return last_reading + MULTIPLIER
        # else:
        return last_reading + (digit * MULTIPLIER) + MULTIPLIER

    if last_digit == 8:

        shutil.move(f1, f2)

        if digit == 0:
            return last_reading + 2 * MULTIPLIER

        if digit != 9:
            return last_reading + (digit * MULTIPLIER) + 2 * MULTIPLIER

    if last_digit > digit:
        return last_reading

    # else:
    shutil.move(f1, f2)
    
    return last_reading + (digit - last_digit) * MULTIPLIER
