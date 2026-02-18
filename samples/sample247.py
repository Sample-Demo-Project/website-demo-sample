from flask import Flask, request, jsonify

app = Flask(__name__)

# [1] request.method
@app.route("/method-demo", methods=["GET", "POST"])
def method_demo():
    return jsonify({
        "method": request.method
    })


# [2] request.args
@app.route("/search")
def search():
    keyword = request.args.get("q")
    page = request.args.get("page", 1)

    return jsonify({
        "keyword": keyword,
        "page": page
    })


# [3] request.json
@app.route("/add", methods=["POST"])
def add():
    data = request.json

    return jsonify({
        "received_json": data,
        "result": data["a"] + data["b"]
    })


# [4] request.form
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    return jsonify({
        "username": username,
        "password": password
    })


# [5] request.headers
@app.route("/headers")
def headers():
    return jsonify({
        "User-Agent": request.headers.get("User-Agent"),
        "Content-Type": request.headers.get("Content-Type")
    })


# [6] request.path
@app.route("/path-demo")
def path_demo():
    return jsonify({
        "path": request.path
    })


# [7] request.url
@app.route("/url-demo")
def url_demo():
    return jsonify({
        "url": request.url
    })


# [8] request.remote_addr
@app.route("/ip")
def get_ip():
    return jsonify({
        "client_ip": request.remote_addr
    })


if __name__ == "__main__":
    app.run()
