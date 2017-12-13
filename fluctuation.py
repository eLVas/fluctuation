import numpy as np
from scipy.optimize import curve_fit

def test(arr, i, v, match):
    if type(match) != list:
        return v == match
    else:
        n = len(match)
        if len(arr) < i+n:
            return False
        return arr[i:i+n] == match

def encode(arr, match):
    res = []
    for i, v in enumerate(arr):
        if type(v) == list:
            res += encode(v, match)
        else:
            m = test(arr, i, v, match)
            res.append(int(m))

    return res

def encode_vocab(arr):
    voc = set()
    r = []

    for w in text:
        if w in voc:
            r.append(0)
        else
            r.append(1)

    return r


def calculate(arr, w, step=None):
    n = len(arr)
    s = step or w
    m = [sum(arr[i:i+w]) for i in range(0, n, s) if i+w < n]
    return np.mean(m), np.std(m)


def run(arr, min_l, max_l, increment, step=None, callback=None):
    res = []

    for i in range(min_l, max_l, increment):
        st = step or i
        mean, std = calculate(arr, i, st)
        res.append((i, mean, std))
        if callback:
            callback(i, mean, std)

    return res

def cost_function(x, a, b, c):
    return c + b*x**a

def get_gamma(x,y):
    return curve_fit(cost_function, x, y, maxfev = 10000)[0]
