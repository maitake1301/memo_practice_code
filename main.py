import os
from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route("/")
def home():
    files = os.listdir("memo")
    return render_template("index.html",files=files)

@app.route("/view/<filename>")
def view(filename):
    with open(f"memo/{filename}", "r", encoding="utf-8") as file:
        memo = file.read()
    return render_template(
    "view.html",
    memo=memo,
    filename=filename
)


@app.route("/save", methods=["POST"])
def save():

    title = request.form["title"]
    memo = request.form["memo"]

    with open(f"memo/{title}.txt", "w", encoding="utf-8") as file:
        file.write(memo)

    return render_template("success.html")

@app.route("/delete/<filename>")
def delete(filename):

    path = f"memo/{filename}"

    if os.path.exists(path):
        os.remove(path)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)