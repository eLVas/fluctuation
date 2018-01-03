При першому використанні необходно запустити install.bat для того щоб встановилися допоміжні бібліотеки

Всі скрипти що починаються з gui запускають програми з графічним інтерфейсом

Також є ще два скрипти які запускаються в консольному режимі з відповідними параметрами

main.py

usage: main.py [-h] [-i TEXT] [-f FILE] [-t TEMPLATE_STRING] [-m MODE]
               [-o OUTPUT_FILE] [-e] [-l MIN_WINDOW_ABSOLUTE]
               [-lp MIN_WINDOW_RELATIVE] [-lm MAX_WINDOW_ABSOLUTE]
               [-lmp MAX_WINDOW_RELATIVE] [-wi WINDOW_INCREMENT_ABSOLUTE]
               [-wip WINDOW_INCREMENT_RELATIVE] [-ws WINDOW_STEP] [-c] [-s]

main

optional arguments:
  -h, --help            show this help message and exit
  -i TEXT               input text
  -f FILE               path to file that should be used as input
  -t TEMPLATE_STRING    template, for n-grams will be separated on whitespace
  -m MODE               char - characters, word - words, prep - preprocessed
  -o OUTPUT_FILE        save output to provided file
  -e                    do not do fluctuation analysis only encode text as 0
                        and 1 sequence
  -l MIN_WINDOW_ABSOLUTE
                        starting window size
  -lp MIN_WINDOW_RELATIVE
                        starting size of window as percent from text size
  -lm MAX_WINDOW_ABSOLUTE
                        maximum window size
  -lmp MAX_WINDOW_RELATIVE
                        maximum size of window as percent from text size
  -wi WINDOW_INCREMENT_ABSOLUTE
                        window size increment step
  -wip WINDOW_INCREMENT_RELATIVE
                        window size increment step
  -ws WINDOW_STEP       window step, default - the same as window size
  -c                    case sensitive flag
  -s                    include separators when matching n-grams, whitespace
                        for characters mode and end of sentance for words mode

run_all_vocab.py

usage: run_all_vocab.py [-h] [-i TEXT] [-f FILE] [-n NGRAM] [-m MODE]
                        [-o OUTPUT_FILE] [-e] [-d MIN_DICTIONARY_ABSOLUTE]
                        [-dp MIN_DICTIONARY_RELATIVE]
                        [-dm MAX_DICTIONARY_ABSOLUTE]
                        [-dmp MAX_DICTIONARY_RELATIVE]
                        [-l MIN_WINDOW_ABSOLUTE] [-lp MIN_WINDOW_RELATIVE]
                        [-lm MAX_WINDOW_ABSOLUTE] [-lmp MAX_WINDOW_RELATIVE]
                        [-wi WINDOW_INCREMENT_ABSOLUTE]
                        [-wip WINDOW_INCREMENT_RELATIVE] [-ws WINDOW_STEP]
                        [-c] [-s] [-p]

run all vocab

optional arguments:
  -h, --help            show this help message and exit
  -i TEXT               input text
  -f FILE               path to file that should be used as input
  -n NGRAM              n in n-grams
  -m MODE               char - characters, word - words, prep - preprocessed
  -o OUTPUT_FILE        save output to provided file
  -e                    do not do fluctuation analysis only encode text as 0
                        and 1 sequence
  -d MIN_DICTIONARY_ABSOLUTE
                        minimal number of ocurances for word
  -dp MIN_DICTIONARY_RELATIVE
                        minimal relative frequency for word
  -dm MAX_DICTIONARY_ABSOLUTE
                        maximum number of ocurances for word
  -dmp MAX_DICTIONARY_RELATIVE
                        maximum relative frequency for word
  -l MIN_WINDOW_ABSOLUTE
                        starting window size
  -lp MIN_WINDOW_RELATIVE
                        starting size of window as percent from text size
  -lm MAX_WINDOW_ABSOLUTE
                        maximum window size
  -lmp MAX_WINDOW_RELATIVE
                        maximum size of window as percent from text size
  -wi WINDOW_INCREMENT_ABSOLUTE
                        window size increment step
  -wip WINDOW_INCREMENT_RELATIVE
                        window size increment step
  -ws WINDOW_STEP       window step, default - the same as window size
  -c                    case sensitive flag
  -s                    include separators when matching n-grams, whitespace
                        for characters mode and end of sentance for words mode
  -p                    remove punctuation


