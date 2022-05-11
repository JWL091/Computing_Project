# ==================================================
# Validation program
# This program validates data
# Written J Lockett                  09/05/2022
# ===================================================


# Length validation
# Checks if the length of data matches the required length
# Decides required based on the value of option passed into it
# Returns True or false depending

def validate_length(data, length, option):
    if option == 1:
        if len(data) == length:
            return True
        else:
            return False
    elif option == 2:
        if len(data) >= length:
            return True
        else:
            return False
    else:
        if len(data) < length:
            return True
        else:
            return False


# Range validation

def validate_range(data, hi, lo):
    #code to check data between hi and lo
    if range(data) == data(hi) - data(lo):
        return True
    else:
        return False
    #return True/False


# Testing
if __name__ == "__main__":
    print(validate_length("Hello there", 11, 1))
    print(validate_length("Good", 3, 2))
    print(validate_length("Many words", 12, 3))
    print(validate_length("Fishing", 8, 1))
    print(validate_length("Forty", 10, 2))
    print(validate_length("Twenty", 5, 3))