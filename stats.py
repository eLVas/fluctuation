def flatten(arr):
    return [item for sublist in arr for item in sublist]

def get_n_grams(text_arr, n):
    if type(text_arr[0]) == list:
        return flatten([get_n_grams(l, n) for l in text_arr])
    else:
        tz = [[None]*i + text_arr for i in range(n)][::-1]
        return [z for z in zip(*tz) if z[0]]

def vocab(text_arr, n):
    return list(set(get_n_grams(text_arr, n)))

def test(arr, i, v, match):
    if type(match) != list:
        return v == match
    else:
        n = len(match)
        if len(arr) < i+n:
            return False
        return arr[i:i+n] == match

def count_ocurences(arr, match):
    c = 0
    for i, v in enumerate(arr):
        if type(v) == list:
            c += count_ocurences(v, match)
        else:
            if test(arr, i, v, match):
                c += 1
    return c

def to_relative(freq, n):
    return {k: v/n for k, v in freq.items()}

def relative_frequency(text_arr, n=1, word=None):
    text_length = len(text_arr)
    if word :
        return frequency(text_arr, n, word)/text_length

    return to_relative(frequency(text_arr, n), text_length)

def frequency(text_arr, n=1, word=None):
    if word :
        return count_ocurences(text_arr, word)

    words = vocab(text_arr, n)
    freq = {}
    for w in words:
        wl = list(w)
        freq[' '.join(wl)] = frequency(text_arr, n, wl)

    return freq
