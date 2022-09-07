from flask import *

app = Flask(__name__)
app.config["Debug"] = True


@app.route('/')
def mydef():
    return "hello page"
if __name__ == '__main__':
    app.run()