from flask import Flask, request, jsonify

app = Flask(__name__)

items = {
    1: {"id": 1, "name": "Pen"},
    2: {"id": 2, "name": "Book"}
}


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, PUT, PATCH, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.put("/items/<int:item_id>")
def replace_item(item_id):
    data = request.get_json(silent=True) or {}
    name = data.get("name", "")
    items[item_id] = {"id": item_id, "name": name}
    return jsonify(items[item_id])


@app.patch("/items/<int:item_id>")
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "not found"}), 404

    data = request.get_json(silent=True) or {}
    if "name" in data:
        items[item_id]["name"] = data["name"]

    return jsonify(items[item_id])


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "not found"}), 404

    items.pop(item_id)
    return "", 204


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
