# import the library
from appJar import gui
import main


app = gui("Flunctuation axprox analysis", "700x200")

def cast_str_to_none(val, parse_float=True):
    return (float(val) if parse_float else val) if len(val) > 0 else None

# handle button events
def run(button):
    props = app.getAllEntries()

    l = []

    data = main.read_tsv(props['file'])
    popv = main.approx(data)

    print(popv)

    if len(props['Output file']) > 0:
        main.write_to_file(props['Output file'], [popv], False)


def create_app_ui(app):
    # create a GUI variable called app
    app.setFont(18)

    app.addLabel("l_file", "Input file")
    app.setLabelAlign("l_file", "left")
    app.addFileEntry("file")

    app.addLabelEntry("Output file")

    # link the buttons to the function called press
    app.addButtons(["Calculate"], run)

    # start the GUI
    app.go()

create_app_ui(app)
