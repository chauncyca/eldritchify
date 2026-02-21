from flask import Flask, request, jsonify
from flask_cors import CORS

import eldritchify as e

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=["GET", "POST"])
def gfg():
    try:
        data = request.json
        text = data.get('text', '')

        result = e.curseText(text)

        return jsonify({'result': result})

    except:
        return ""

if __name__ == "__main__":
    app.run()
