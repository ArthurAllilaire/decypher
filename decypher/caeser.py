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