import store
from fastapi import FastAPI  # type: ignore
from fastapi.responses import HTMLResponse # type: ignore

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3]

@app.get("/contact", response_class=HTMLResponse)
def get_name():
    return """
    <h1>Hola soy una pagina web</h1>
    <p>Esta es una pagina web de prueba</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()