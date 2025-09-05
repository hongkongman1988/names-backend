from flask import Flask, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

NAMES_FILE = "names.txt"

@app.route("/names", methods=["GET"])
def get_names():
    if not os.path.exists(NAMES_FILE):
        return "", 200
    return send_file(NAMES_FILE, mimetype="text/plain")

@app.route("/names", methods=["POST"])
def save_names():
    data = request.data.decode("utf-8")
    with open(NAMES_FILE, "w", encoding="utf-8") as f:
        f.write(data)
    return "Names updated successfully"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)