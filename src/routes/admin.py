from flask import jsonify
from src.app import app


@app.route("/v1/admin")
def admin_route():
    return jsonify({
        "status": 200,
        "message": "Admin route works!"
    }), 200


@app.route("/v1/admin/<user_id>")
def admin_route_user_id(user_id):
    return jsonify({
        "status": 200,
        "message": f'Admin route works for user {user_id}!'
    }), 200
