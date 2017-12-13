import argparse
import matplotlib.pyplot as plt

import preprocessor
import fluctuation
# import stats

param_keys_map = [
    ('case_sensative', None),
    ('separators', None),
    ('punctuation', None)
]

l_param_keys_map = [
    ('min_window_absolute', 'l_min'),
    ('min_window_relative', 'l_min_rel'),
    ('max_window_absolute', 'l_max'),
    ('max_window_relative', 'l_max_rel'),
    ('window_increment_absolute', 'increment'),
    ('window_increment_relative','increment_relative'),
    ('window_step','step')
]


def read_whole_file(input_path):
    text = ""
    with open(input_path) as f:
        for line in f:
            text += line

    return text


def pick(d, keys):
    return {key or key_old: d[key_old] for key_old, key in keys }


def run(args):

    print(args)

    text = args['text'] or read_whole_file(args['file'])
    template = ( args['template_string'] if args['case_sensative'] else args['template_string'].lower() ).split()

    params = pick(args, param_keys_map)
    l_params = pick(args, l_param_keys_map)

    analyse(text, args['mode'], l_params, template, preprocessor_params=params)


def analyse(text, mode, l, template, preprocessor_params):

    prep_text = preprocessor.prepare(text, mode, **preprocessor_params)

    print('text legth: ',len(prep_text))

    """
    vocab = sorted(stats.vocab(prep_text))
    freq = stats.relative_frequency(prep_text)

    print(vocab)
    print()

    for key in sorted(freq, key=lambda x: freq[x]):
        print("{0}: {1:1.5f}".format(key, freq[key]))
    """
    print()

    # print(prep_text)

    encoded_text = fluctuation.encode(prep_text, template)

    # print(encoded_text)

    x = []
    y = []

    l_full = len(encoded_text)

    min_l = int(l['l_min'] or l_full*l['l_min_rel'])
    max_l = int(l['l_max'] or l_full*l['l_max_rel'])
    increment = int(l['increment'] or (max_l-min_l)*l['increment_relative'])

    print('min_l: ', min_l)
    print('max_l: ', max_l)
    print('l_increment: ', increment)
    print('w_step: ', l['step'])
    print()

    print('L\tmean\tstd')

    res = fluctuation.run(
        encoded_text,
        min_l, max_l,
        increment,
        int(l['step']),
        lambda i, mean, std: print('{0:2d}\t{1:2.2f}\t{2:2.2f}'.format(i, mean, std))
    )

    res_plot = list(zip(*res))

    popt = fluctuation.get_gamma(res_plot[0], res_plot[2])
    print(popt)
    print('\ngama: ', popt[0])

    plt.plot(res_plot[0], res_plot[2])

    tabl = range(res_plot[0][0], res_plot[0][-1], int(abs(res_plot[0][0] - res_plot[0][-1])/1000))
    plt.plot(tabl, fluctuation.cost_function(tabl, *popt), 'g--')

    plt.show()


if __name__ == '__main__':

    def build_args_parser():
        parser = argparse.ArgumentParser(
            description='This is a PyMOTW sample program',
        )

        parser.add_argument('-i', action="store",       dest="text",                              help="input text")
        parser.add_argument('-f', action="store",       dest="file",                              help="path to file that should be used as input")
        # parser.add_argument('-p', action="store_true",  dest="preprocessed",                       help="input is preprocessed and is a sequence of 0 and 1")
        parser.add_argument('-t', action="store",       dest="template_string",                   help="template, for n-grams will be separated on whitespace")
        parser.add_argument('-m', action="store",       dest="mode",              default='char', help="char - characters, word - words, prep - preprocessed")

        parser.add_argument('-l',   action="store", dest="min_window_absolute",         type=int,                   help="starting window size")
        parser.add_argument('-lp',  action="store", dest="min_window_relative",         type=float, default=0.01,   help="starting size of window as percent from text size")
        parser.add_argument('-lm',  action="store", dest="max_window_absolute",         type=int,                   help="maximum window size")
        parser.add_argument('-lmp', action="store", dest="max_window_relative",         type=float, default=0.05,    help="maximum size of window as percent from text size")
        parser.add_argument('-wi',  action="store", dest="window_increment_absolute",   type=int,                   help="window size increment step")
        parser.add_argument('-wip',  action="store", dest="window_increment_relative",  type=float, default=0.1,    help="window size increment step")
        parser.add_argument('-ws',  action="store", dest="window_step",                 type=int,                   help="window step, default - the same as window size")

        parser.add_argument('-c', action="store_true", dest="case_sensative",   help="case sensative flag")
        parser.add_argument('-s', action="store_true", dest="separators",       help="include separators when matching n-grams, whitespace for characters mode and end of sentance for words mode")
        parser.add_argument('-p', action="store_true", dest="punctuation",      help="remove punctuation")

        return parser


    parser = build_args_parser()
    args = parser.parse_args()
    vargs = vars(args)

    run(vargs)