def vocab(text_arr):
    return list(set(text_arr))


def count_ocuurences(text_arr, word):
    c = 0
    for e in text_arr:
        if e == word:
            c += 1
    return c

def to_relative(freq, n):
    return {k: v/n for k, v in freq.items()}

def relative_frequency(text_arr, word=None):
    n = len(text_arr)

    if word :
        return frequency(text_arr, word)/n

    return to_relative(frequency(text_arr), n)

def frequency(text_arr, word=None):
    if word :
        return count_ocuurences(text_arr, word)

    words = vocab(text_arr)
    freq = {}
    for w in words:
        freq[w] = frequency(text_arr, w)

    return freq
