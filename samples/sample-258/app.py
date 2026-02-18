from flask import Flask, request, jsonify

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/form-submit", methods=["OPTIONS"])
def form_preflight():
    return "", 204


@app.post("/form-submit")
def form_submit():
    name = request.form.get("name", "")
    email = request.form.get("email", "")

    return jsonify({
        "status": "ok",
        "received": {
            "name": name,
            "email": email
        }
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
