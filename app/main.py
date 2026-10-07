from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"status": "healthy", "service": "python-api"}), 200

    @app.route("/api/v1/resource", methods=["GET"])
    def get_resource():
        return jsonify({
            "id": "res-101",
            "name": "DevOps Container Demo",
            "active": True
        }), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
