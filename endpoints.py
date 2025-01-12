# endpoints.py

from flask import jsonify, Blueprint

api = Blueprint("api", __name__)

@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Volcan AI is running!"}), 200

def setup_routes(app):
    app.register_blueprint(api, url_prefix="/api")
