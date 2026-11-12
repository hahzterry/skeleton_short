
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "skeleton_short",
        "message": "Vercel API is running"
    })
