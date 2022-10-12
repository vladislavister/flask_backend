from flask import jsonify, request

from app import app

USERS = {
    1: "Johny Bravo",
    2: "Peter Griffin"
}


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route('/users/<id>')
def get_user_by_id(id):
    return USERS[1]


@app.route("/users", methods=['POST'])
def create_user():
    request_data = request.get_json()
    print(request_data)
    return "STATUS: OK"
