from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/certifikacia')
def certifikacia():
    return render_template('certifikacia.html')

@app.route('/dakujem')
def dakujem():
    return render_template('dakujem.html')

if __name__ == '__main__':
    app.run()