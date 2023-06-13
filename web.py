from flask import Flask, render_template, request

htmlFile = "index.html"

app = Flask(__name__)
@app.route("/")
@app.route("/form")
def index():
    with open(htmlFile, "r") as f:
        return f.read() 

@app.route("/data", methods=["POST", "GET"])
def fund():
    if request.method == 'POST':
        form_data = request.form
        return render_template('index.html', form_data = form_data)
    else:
        return "FAil"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)