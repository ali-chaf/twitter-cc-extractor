from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Twitter CC Extractor API is running."


@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()

    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # CC extraction will be added here later
    return jsonify({
        "message": "URL received",
        "url": url
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
