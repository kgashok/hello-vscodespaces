from flask import Flask

app = Flask.run(__name__)

@app.route('/')
def index():
    return "Hello, VS Codespaces!"
