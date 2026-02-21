from flask import Flask

import eldritchify as e

app = Flask(__name__)

@app.route("/")
def hello_world(inStr: str):
    return "<p>" + e.curseText(inStr) + "</p>"

if __name__ == "__main__":
    app.run(debug=True)