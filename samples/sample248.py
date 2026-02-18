from flask import Flask, jsonify, request

app = Flask(__name__)

# 假資料
tasks = [
    {"id": 1, "title": "Study Flask"},
    {"id": 2, "title": "Build API"}
]

# =====================================================
# 傳統寫法 (app.route + methods)
# =====================================================

@app.route("/route/tasks", methods=["GET"])
def route_get_tasks():
    return jsonify(tasks)


@app.route("/route/tasks", methods=["POST"])
def route_create_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Title required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"]
    }

    tasks.append(new_task)
    return jsonify(new_task), 201


# =====================================================
# REST 風格寫法 (Flask 2.0+)
# =====================================================

@app.get("/rest/tasks")
def rest_get_tasks():
    return jsonify(tasks)


@app.post("/rest/tasks")
def rest_create_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Title required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"]
    }

    tasks.append(new_task)
    return jsonify(new_task), 201


# =====================================================
# 啟動
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
