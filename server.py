from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'HOLA - Bienvenido al curso de Telemática - HOLA'

@app.route('/render')
def render():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run (host="0.0.0.0", port=8090)
