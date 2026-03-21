from flask import request, Flask

app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test():
    return f"Method is {request.method}"

if __name__ == "__main__":
    app.run()