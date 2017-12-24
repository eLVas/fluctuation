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

    print(data)

    popv = main.aprox(data)


def create_app_ui(app):
    # create a GUI variable called app
    app.setFont(18)

    # -f file
    app.addLabel("l_file", "Input file")
    app.setLabelAlign("l_file", "left")
    app.addFileEntry("file")

    # link the buttons to the function called press
    app.addButtons(["Calculate"], run)

    # start the GUI
    app.go()

create_app_ui(app)
