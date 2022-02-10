from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h2>HTML Images</h2>"
            "<p>HTML images are defined with the img tag:</p>"
    return html

PORT = int(os.environ.get("PORT", 9090))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8080)
