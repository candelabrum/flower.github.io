from flask import Flask, render_template

app = Flask(__name__, template_folder='.')


@app.route("/")
def web():
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port='3000')
