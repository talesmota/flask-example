from flask import jsonify
from src.app import app


@app.route("/v1/config")
def config_route():
    return jsonify({
        "status": 200,
        "message": "config route works!"
    }), 200


@app.route("/v1/config/<user_id>")
def config_route_user_id(user_id):
    return jsonify({
        "status": 200,
        "message": f'config route works for user {user_id}!'
    }), 200
