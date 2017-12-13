import os
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

def write_sequense(file, data):
    file.write(''.join(map(str,data)))

def write_tab_separated(file, data, header=None):
    if header:
        file.write('\t'.join(header) + '\n')

    for row in data:
        file.write('\t'.join(map(str,row)) + '\n')


def write_to_file(output_path, data, sequence):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w+') as f:
        if sequence:
            write_sequense(f, data)
        else:
            write_tab_separated(f, data)


def pick(d, keys):
    return {key or key_old: d[key_old] for key_old, key in keys }


def run(args):
    # print(args)

    text = args['text'] or read_whole_file(args['file'])
    p_params = pick(args, param_keys_map)
    l_params = pick(args, l_param_keys_map)

    prep_text = preprocessor.prepare(text, args['mode'], **p_params)

    print('text legth: ',len(prep_text))
    print()

    encoded_text = prep_text

    if args['mode'] != 'prep':
        if args['template_string'] is None:
            encoded_text = fluctuation.encode_vocab(prep_text)
        else:
            template = ( args['template_string'] if args['case_sensative'] else args['template_string'].lower() ).split()
            encoded_text = fluctuation.encode(prep_text, template)

    if args['only_encode']:
        if args['output_file']:
            write_to_file(args['output_file'], encoded_text, True)

        return encoded_text, None

    result, gamma = analyse(encoded_text, args['mode'], l_params)

    if args['output_file']:
        write_to_file(args['output_file'], result, False)

    return result, gamma


def analyse(text, mode, l):
    l_full = len(text)

    min_l = int(l['l_min'] or l_full*l['l_min_rel'])
    max_l = int(l['l_max'] or l_full*l['l_max_rel'])
    increment = int(l['increment'] if l['increment'] is not None else (max_l-min_l)*l['increment_relative'])

    print('min_l: ', min_l)
    print('max_l: ', max_l)
    print('l_increment: ', increment)
    print('w_step: ', l['step'])
    print()

    print('L\tmean\tstd')

    res = fluctuation.run(
        text,
        min_l, max_l,
        increment,
        int(l['step']),
        lambda i, mean, std: print('{0:2d}\t{1:2.2f}\t{2:2.2f}'.format(i, mean, std))
    )

    if len(res) < 3:
        return res, None

    res_plot = list(zip(*res))

    popt = fluctuation.get_gamma(res_plot[0], res_plot[2])
    gamma = popt[0]
    print('\ngama: ', gamma)

    plt.plot(res_plot[0], res_plot[2])

    tabl = range(res_plot[0][0], res_plot[0][-1], int(abs(res_plot[0][0] - res_plot[0][-1])/1000))
    plt.plot(tabl, fluctuation.cost_function(tabl, *popt), 'g--')

    plt.show()

    return res, gamma


if __name__ == '__main__':

    def build_args_parser():
        parser = argparse.ArgumentParser(
            description='This is a PyMOTW sample program',
        )

        parser.add_argument('-i', action="store",       dest="text",                              help="input text")
        parser.add_argument('-f', action="store",       dest="file",                              help="path to file that should be used as input")
        parser.add_argument('-t', action="store",       dest="template_string",                   help="template, for n-grams will be separated on whitespace")
        parser.add_argument('-m', action="store",       dest="mode",              default='char', help="char - characters, word - words, prep - preprocessed")
        parser.add_argument('-o', action="store",       dest="output_file",                       help="save output to provided file")
        parser.add_argument('-e', action="store_true",  dest="only_encode",                       help="do not do fluctuation analysis only encode text as 0 and 1 sequence")

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
