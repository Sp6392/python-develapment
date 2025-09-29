from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# --- Routes ---

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# POST add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# PUT update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id].update(data)
    return jsonify(users[user_id])

# DELETE remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
