import argparse

import preprocessor
import stats
import main

def run(args):

    text = args['text'] or main.read_whole_file(args['file'])
    p_params, l_params = main.separate_params(args)
    prep_text = preprocessor.prepare(text, args['mode'], **p_params)

    min_d = (args['min_dictionary_absolute'] or 0)/len(prep_text) or args['min_dictionary_relative']
    max_d = (args['max_dictionary_absolute'] or 0)/len(prep_text) or args['max_dictionary_relative']

    freq = stats.relative_frequency(prep_text)
    vocab = [k for k,v in freq.items() if v >= min_d and v <= max_d]

    res = []

    output_file = args['output_file']

    for v in vocab:
        args['template_string'] = v
        args['output_file'] = None
        _, gamma = main.run(args, False)
        res.append((v, gamma))

    if output_file is not None and len(output_file) > 0:
        main.write_to_file(output_file, res, False)



if __name__ == '__main__':

    def build_args_parser():
        parser = argparse.ArgumentParser(
            description='run all vocab',
        )

        parser.add_argument('-i', action="store",       dest="text",                                help="input text")
        parser.add_argument('-f', action="store",       dest="file",                                help="path to file that should be used as input")
        parser.add_argument('-n', action="store",       dest="ngram",    type=int,  default=1,      help="n in n-grams")
        parser.add_argument('-m', action="store",       dest="mode",                default='char', help="char - characters, word - words, prep - preprocessed")
        parser.add_argument('-o', action="store",       dest="output_file",                         help="save output to provided file")
        parser.add_argument('-e', action="store_true",  dest="only_encode",                         help="do not do fluctuation analysis only encode text as 0 and 1 sequence")

        parser.add_argument('-d',   action="store", dest="min_dictionary_absolute",     type=int,                   help="minimal number of ocurances for word")
        parser.add_argument('-dp',  action="store", dest="min_dictionary_relative",     type=float, default=0.001,  help="minimal relative frequency for word")
        parser.add_argument('-dm',   action="store", dest="max_dictionary_absolute",    type=int,                   help="maximum number of ocurances for word")
        parser.add_argument('-dmp',  action="store", dest="max_dictionary_relative",    type=float, default=0.01,   help="maximum relative frequency for word")

        parser.add_argument('-l',   action="store", dest="min_window_absolute",         type=int,                   help="starting window size")
        parser.add_argument('-lp',  action="store", dest="min_window_relative",         type=float, default=0.01,   help="starting size of window as percent from text size")
        parser.add_argument('-lm',  action="store", dest="max_window_absolute",         type=int,                   help="maximum window size")
        parser.add_argument('-lmp', action="store", dest="max_window_relative",         type=float, default=0.05,   help="maximum size of window as percent from text size")
        parser.add_argument('-wi',  action="store", dest="window_increment_absolute",   type=int,                   help="window size increment step")
        parser.add_argument('-wip',  action="store", dest="window_increment_relative",  type=float, default=0.1,    help="window size increment step")
        parser.add_argument('-ws',  action="store", dest="window_step",                 type=int,                   help="window step, default - the same as window size")

        parser.add_argument('-c', action="store_true", dest="case_sensitive",   help="case sensitive flag")
        parser.add_argument('-s', action="store_true", dest="separators",       help="include separators when matching n-grams, whitespace for characters mode and end of sentance for words mode")
        parser.add_argument('-p', action="store_true", dest="punctuation",      help="remove punctuation")

        return parser


    parser = build_args_parser()
    args = parser.parse_args()
    vargs = vars(args)

    run(vargs)
