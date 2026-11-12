from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Cloud Technologies</h1>
    <p>My first Docker application</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
