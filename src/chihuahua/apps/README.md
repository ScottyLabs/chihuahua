This folder stores several subcomponents of the app.
These include
* [`health_check`](health_check.py), which can check the status of app services
* [`admin`](admin.py), which provides administrative settings
* [`form`](form.py), which is where winners fill out their information

Modularizing the app this way can allow for easier testability and modularization
(not all pages have to be declared in one place, and you can run an individual app to test it if you want).

## Example

The basic structure of an app looks something like this

*hello.py*
```python
# probably included through a broader import
from fasthtml.fastapp import fast_app

hello_app, rt = fast_app()

@rt('/')
def get():
  return 'Hello world!'
```

and this can now be wired up into the main app, looking something like this

*main.py*
```python
from fasthtml.fastapp import fast_app
from fasthtml.starlette import Mount

from hello import hello_app

app, rt = fast_app()
app.mount("/hello", hello_app, name="hello")
```

Now, `/hello` will return "Hello world!"