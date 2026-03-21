from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.post("/message")
def message():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Anonymous")
    message_text = data.get("message", "")

    return jsonify({
        "status": "ok",
        "received": {
            "name": name,
            "message": message_text
        }
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
