#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!" 

@app.route('/user')
def user():
    user = {'nick': 'Leo',
            'name': 'Leandro'}  # fake user
    return '''<!DOCTYPE html>
<html>
<head>
<title>Usuario {nick}</title>
</head>
<body>

<h1>Hola {usuario}</h1>
<p>Está bastante bueno esto de Flask.</p>

</body>
</html> 
'''.format(usuario=user['name'], nick=user['nick'])

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
