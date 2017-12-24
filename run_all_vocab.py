import os
import argparse
import matplotlib.pyplot as plt

import preprocessor
import fluctuation
import stats
import main

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




def run(args):
    text = args['text'] or read_whole_file(args['file'])
    prep_text = preprocessor.prepare(text, args['mode'], **p_params)

    vocab = stats.vocab(text)

    for v in vocab:
        return main.run()



if __name__ == '__main__':

    def build_args_parser():
        parser = argparse.ArgumentParser(
            description='This is a PyMOTW sample program',
        )

        parser.add_argument('-i', action="store",       dest="text",                              help="input text")
        parser.add_argument('-f', action="store",       dest="file",                              help="path to file that should be used as input")
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
