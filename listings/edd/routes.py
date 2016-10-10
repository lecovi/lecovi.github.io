#!/usr/bin/env python

# Importamos del módulo flask la clase Flask que creará nuestra aplicación.
from flask import Flask

# Creamos una nueva instancia de Flask y la asignamos a `app`.
app = Flask(__name__)

# Estos decoradores nos sirven para mapear qué funciones se van a llamar en el
# momento que al servidor le llegue una petición con esa URL.
@app.route('/')
@app.route('/index')
def index():
    """ Nuestra función que responde en '/' o en '/index' y devuelve un
        simple 'Hello World!'
    """
    return "<h1>Hello World!</h1>"

# Si ejecutamos el módulo, la aplicación de Flask corre con el modo de prueba
# activo.
if __name__ == "__main__":
    app.run(debug=True)
