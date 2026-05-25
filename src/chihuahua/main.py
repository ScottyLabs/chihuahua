from fasthtml.common import *

import sys
is_debug = "--debug" in sys.argv

# this is the super important function called by the root to start the server
def start_server():
    serve(
        reload=is_debug,  # this will watch directory for changes, and reload app.
        # coupled with live reloading, you'll see changes instantly in browser.
        # disabled during deployment because the server gets killed anyway.
        app="app",
        appname="chihuahua.main",
    )

# to enable this, we're not allowed to use relative import
if __name__ == "__main__":
    start_server()

# the rest of the file is dedicated to initializing the server, mounting components,
# and otherwise configuring the app variable that defines what gets run

# must use chihuahua.<something> imports in this file to enable running the file directly
from chihuahua.apps.health_check import health_check_app

app, rt = fast_app(
    live=is_debug, # enable live reloading
    debug=is_debug, # enable extended tracebacks on error
    static_path="./static"
)

app.mount("/health-check", health_check_app, name="health_check")

@rt("/")
def get():
    return Titled("Chihuahua", (
        P("Let's do this!"),
        Div(
            hx_get="/health-check",
            hx_trigger='load',
            hx_swap='outerHTML',
        ),
        A(P("View server health"), href="/health-check"),
    ))