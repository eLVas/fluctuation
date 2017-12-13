import nltk
import string
import re

def remove_new_line_chars(text):
    return text.replace('\r', ' ').replace('\n', ' ')


def remove_whitespaces(text):
    return text.replace(' ', '')


def remove_punctuation(text):
    return re.sub(r'[^\w\s]','',text)

def remove_all_non_letters(text):
    return ''.join([i for i in text if i.isalpha() or i == ' '])


def prepare_words_break_by_sent(text, punctuation=False):
    arr = []

    for sent in nltk.sent_tokenize(text):
        s = sent

        if not punctuation :
            s = remove_punctuation(s)

        arr.append(nltk.word_tokenize(s))

    return arr


def prepare_words_flat(text, punctuation=False):
    t = text

    if not punctuation :
        t = remove_punctuation(t)

    return nltk.word_tokenize(t)


def prepare_words(text, separators=False, punctuation=False, case_sensative=False):
    t = text

    if not case_sensative :
        t = t.lower()

    # not breacking n-grams on sentance separators
    if not separators:
        return prepare_words_flat(t, punctuation=punctuation)

    # breacking n-grams on sentance separators
    return prepare_words_break_by_sent(t, punctuation)


def prepare_chars(text, separators=False, punctuation=False, case_sensative=False):
    t = text

    t = remove_all_non_letters(t)

    if not separators :
        t = remove_whitespaces(t)

    if not case_sensative :
        t = t.lower()

    return list(t)

def prepare_symbols(text, separators=False, punctuation=False, case_sensative=False):
    t = text
    if not separators :
        t = remove_whitespaces(t)

    if not punctuation :
        t = remove_punctuation(t)

    if not case_sensative :
        t = t.lower()

    return list(t)


def restore_preprocessed(text, separators=False, punctuation=False, case_sensative=False):
    return [int(c) for c in text]


preprocessors = {
    'char': prepare_chars,
    'symb': prepare_symbols,
    'word': prepare_words,
    'prep': restore_preprocessed
}


def prepare(text, mode, **kwargs):
    t = text
    t = remove_new_line_chars(t)
    return preprocessors[mode](t, **kwargs)
