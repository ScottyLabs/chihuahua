from fasthtml.common import *
from fasthtml.starlette import Mount

import sys

is_debug = "--debug" in sys.argv

from apps.health_check import health_check_app

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

if __name__ == "__main__":
    serve(
        reload=is_debug, # this will watch directory for changes, and reload app.
                        # coupled with live reloading, you'll see changes instantly in browser.
                        # disabled during deployment because the server gets killed anyway.
    )