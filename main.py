from fasthtml.common import *

import sys

is_debug = "--debug" in sys.argv

app, rt = fast_app(
    live=is_debug, # enable live reloading
    debug=is_debug, # enable extended tracebacks on error
    static_path="./static"
)

@rt("/")
def get():
    return Titled("Chihuahua", P("Let's do this!"))

if __name__ == "__main__":
    serve()