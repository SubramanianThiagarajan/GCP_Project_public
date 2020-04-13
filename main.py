from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def say_hello():
    page = render_template('index.html')
    return page


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
