from time import sleep

from fasthtml.common import *

health_check_app, rt = fast_app()

@health_check_app.get("/")
def main_page(request):
    prefix = request.scope.get("root_path", '')
    return (*((Title("Health Check"),) if not 'hx-request' in request.headers else ()),
            H1("Health Check"),
            Div(
                (
                    H2("Database"),
                    P("Loading...", cls="htmx-indicator"),
                ),
                hx_get=f"{prefix}/db",
                hx_trigger='load',
                hx_on__after_request="this.children[1].remove()",
                hx_swap='beforeend'
            ))

@health_check_app.get("/db")
def db_page(request):
    sleep(3)
    if 'hx-request' in request.headers:
        return P("All good!")
    else:
        return Titled("Database Health Check", P("All good!"))

