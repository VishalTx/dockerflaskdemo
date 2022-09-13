from flask import *
import os
import socket

app = Flask(__name__)

# app.config["Debug"] = True

@app.route('/')
def mydef():
    return "hello page this is python application"
if __name__ == '__main__':
    app.run()


PORT = int(os.environ.get("PORT", 9090))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9090)
