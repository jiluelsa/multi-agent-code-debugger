from flask import Flask, render_template, request
from run_pipeline import run_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    input_code = ""

    if request.method == "POST":
        # Textbox input
        input_code = request.form.get("code", "")

        # File upload input
        uploaded_file = request.files.get("file")
        if uploaded_file and uploaded_file.filename.endswith(".py"):
            input_code = uploaded_file.read().decode("utf-8")

        if input_code.strip():
            output = run_pipeline(input_code)

    return render_template("index.html", input_code=input_code, output=output)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
