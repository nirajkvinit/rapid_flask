from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/goodbye')
def goodbye():
    return "Goodbye world!"

@app.route("/hello/<name>/<int:age>")
def hello_name(name, age):
    return "Hello, {}, You are {} years old.".format(name, age)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
