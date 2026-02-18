from flask import Flask, request, jsonify

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.get("/search")
def search():
    q = request.args.get("q", "python")
    page = request.args.get("page", "1")
    return jsonify({
        "keyword": q,
        "page": int(page) if str(page).isdigit() else page
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
