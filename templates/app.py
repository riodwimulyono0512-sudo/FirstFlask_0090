from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    varNama = request.form.get("parName")
    if not varNama:
        varNama = "Anonim"
    return f"<h2>Halo, {varNama}! Selamat datang di Flask First App 🚀</h2>"

if __name__ == "__main__":
    app.run(debug=True)
    