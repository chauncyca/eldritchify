from flask import Flask, request, render_template

import eldritchify as e

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = "user_input" in HTML form
        user_text = request.form.get("user_input")

        processed_text = e.curseText(user_text)
        return render_template("form.html", result=processed_text)

    # For GET request, render the form page
    return render_template("form.html")

if __name__ == "__main__":
    app.run(port=8083)