from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

@app.route("/check")
def check():
    user_id = request.args.get("user")

    if not user_id:
        return jsonify(ok=False)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember"
    params = {
        "chat_id": CHANNEL_ID,
        "user_id": user_id
    }

    r = requests.get(url, params=params).json()

    if r.get("ok") and r["result"]["status"] in (
        "member", "administrator", "creator"
    ):
        return jsonify(ok=True)

    return jsonify(ok=False)

@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":
    app.run()
