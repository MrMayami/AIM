# This file defines the application routes.
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def interface(template):
    app.run(debug=True)
    render_template('index.html', inerface=template)