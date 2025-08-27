from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pag1')
def pag1():
    return render_template('pag1.html')


if __name__ == '__main__':
    app.run(debug=True)
