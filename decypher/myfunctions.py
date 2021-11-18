import matplotlib.pyplot as plt
import statistics
import string

letter_freq = "etaoinshrdlucwmfygpbvkxjqz"

def caeser_shift(text, shift):
    """ For every letter  """
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                ASCII_START = 65
            else:
                ASCII_START = 96
            new_num = ((ord(char)-ASCII_START)+shift) % 26
            new_char = chr(new_num+ASCII_START)
        else:
            new_char = char
        result.append(new_char)
    return "".join(result)