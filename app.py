from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from profanity_filter import contains_bad_language

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.form["message"]
    if contains_bad_language(user_msg):
        return jsonify({"answer": "⚠️ Please avoid inappropriate language."})
    answer = get_response(user_msg)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
