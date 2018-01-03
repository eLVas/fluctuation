# import the library
from appJar import gui
import run_all_vocab as main


app = gui("Flunctuation analysis for all words", "700x700")

def cast_str_to_none(val, parse_float=True):
    return (float(val) if parse_float else val) if len(val) > 0 else None

# handle button events
def run(button):
    props = app.getAllEntries()
    options = app.getAllOptionBoxes()
    flags = app.getAllCheckBoxes()

    main.run({
        "text": None,
        "file": props['file'],
        "ngram": props['N-grams'],
        "mode": options['Modes'],
        "min_window_absolute": cast_str_to_none(props['Min(absolute)']),
        "min_window_relative": cast_str_to_none(props['Min(relative)']),
        "max_window_absolute": cast_str_to_none(props['Max(absolute)']),
        "max_window_relative": cast_str_to_none(props['Max(relative)']),
        "min_dictionary_absolute": cast_str_to_none(props['Min_frequency(absolute)']),
        "min_dictionary_relative": cast_str_to_none(props['Min_frequency(relative)']),
        "max_dictionary_absolute": cast_str_to_none(props['Max_frequency(absolute)']),
        "max_dictionary_relative": cast_str_to_none(props['Max_frequency(relative)']),
        "window_increment_absolute": cast_str_to_none(props['Increment(absolute)']),
        "window_increment_relative": cast_str_to_none(props['Increment(relative)']),
        "window_step": cast_str_to_none(props['Step']),
        "case_sensitive": flags['Case sensitive'],
        "separators": flags['Separators'],
        "output_file": props["Output file"],
        "only_encode": False
    })

def create_app_ui(ap,modes):
    # create a GUI variable called app
    app.setFont(18)

    # -f file
    app.addLabel("l_file", "Input file")
    app.setLabelAlign("l_file", "left")
    app.addFileEntry("file")

    # -n template_string
    app.addLabelEntry("N-grams")

    # -m mode
    app.addLabelOptionBox("Modes", modes)

    #window size
    with app.labelFrame("Dictionary"):
        # -l min_window_absolute
        app.addLabelEntry("Min_frequency(absolute)")
        # -lp min_window_relative
        app.addLabelEntry("Min_frequency(relative)")
        app.setEntry("Min_frequency(relative)", "0.001")
        # -lm max_window_absolute
        app.addLabelEntry("Max_frequency(absolute)")
        # -lmp max_window_relative
        app.addLabelEntry("Max_frequency(relative)")
        app.setEntry("Max_frequency(relative)", "0.01")

    #window size
    with app.labelFrame("Window size"):
        # -l min_window_absolute
        app.addLabelEntry("Min(absolute)")
        # -lp min_window_relative
        app.addLabelEntry("Min(relative)")
        app.setEntry("Min(relative)", "0.01")
        # -lm max_window_absolute
        app.addLabelEntry("Max(absolute)")
        # -lmp max_window_relative
        app.addLabelEntry("Max(relative)")
        app.setEntry("Max(relative)", "0.2")

    #window step and increment
    with app.labelFrame("Window step and increment"):
        # -wi window_increment_absolute
        app.addLabelEntry("Increment(absolute)")
        # -wip window_increment_relative
        app.addLabelEntry("Increment(relative)")
        app.setEntry("Increment(relative)", "0.01")
        # -ws window_step
        app.addLabelEntry("Step")
        app.setEntry("Step", "100")

    #flags
    with app.labelFrame("Flags"):
        # -c case_sensitive
        app.addCheckBox("Case sensitive")
        # -s separators
        app.addCheckBox("Separators")

    # -o output_file
    app.addLabelEntry("Output file")


    # link the buttons to the function called press
    app.addButtons(["Calculate"], run)

    # start the GUI
    app.go()


modes = ['alph', 'symb', 'word', 'prep']

create_app_ui(app, modes)
