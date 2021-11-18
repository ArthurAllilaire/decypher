import string
import statistics
from cypher import letter_freq, get_freq_vals, 

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


def find_nth(haystack, needle, n):
    """ Code copied from  https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string - read more there about the comparisons of speed of different solutions."""
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def brute_force_ceaser(text, num_words=0):
    """ Takes in the text that has been encrypted with a ceaser shift, returns both the decrytpted text and ceaser shift. Can specify a number of words to take to iterate over instaed of the default first sentence. """
    # Lets use only the first sentence
    if not num_words:
        # Slice the string to get the first sentence
        sentence = text[0:text.index(".")]
    else:
        sentence = text[0:find_nth(text, " ", num_words)]

    for i in range(26):
        decrypted = caeser_shift(sentence, i)
        print(decrypted, i)

def get_shift(letter1, letter2):
    shift = ord(letter2.lower()) - ord(letter1.lower())
    # Don't want to have negative shifts
    if shift < 0:
        return shift + 26

    return shift


def get_modal_shift(letters, letter_freq=letter_freq):
    shift = []
    for i in range(len(letters)):
        shift.append(get_shift(letters[i], letter_freq[i]))

    print(shift)

    return round(statistics.mode(shift))


def FQ_ceaser(text, letter_freq="etaoinshrdlucwmfygpbvkxjqz"):
    """TAkes the text that has been shifted. Calls the frequency_analysis and from the top 5 letters figures out the most likely shift."""
    # Get the frequency dict
    FQ_List = list(get_freq_vals(text))
    letters_missing = 26-len(FQ_List)
    if letters_missing:
        # Assume the letters missing are the least frequent
        if letters_missing == 1:
            # Add the missing letter
            alphabet = list(string.ascii_lowercase)
            for char in FQ_List:
                alphabet.remove(char.lower())
            # The last one left is the last letter
            FQ_List.append(alphabet[0])
            print(alphabet)
        else:
            # If there are more than 1 cut letter_freq by the amount of missing letters (shift the letters that are compared so its the 6 least frequent letters that appear rather than overall).
            letter_freq = letter_freq[:-letters_missing]

    # Get the top 5 letters of the frequency analysis
    top_letters = FQ_List[:5]
    # Get the bottom 6 letters of the FQ
    bottom_letters = FQ_List[-5:]
    # Get the modal shift for the 5 most frequent and 6 least frequent letters
    shift = get_modal_shift(
        top_letters+bottom_letters, letter_freq[:5]+letter_freq[-5:])
    return shift
