def is_pangram(sentence=None):
    if sentence:
        # convert sentence to lower case
        lower_sent = sentence.lower()

        # convert sentence to Set() to list all unique characters present
        lower_sent = set(lower_sent)

        # separate out all alphabets
        alphabet = [ ch for ch in lower_sent if ord(ch) in range(ord('a'), ord('z')+1)]

        if len(alphabet) == 26:
            return True
        else:
            return False
    else:
        return False


