from flask import Flask, render_template, request, jsonify, session
from chatbot import get_response
from profanity_filter import contains_bad_language
import random

app = Flask(__name__)
app.secret_key = "hackathon_secret"

# Mock email OTP verification
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    otp = random.randint(100000, 999999)
    session["otp"] = str(otp)
    session["email"] = email
    return f"OTP sent to {email} (Mock): {otp}"

@app.route("/verify", methods=["POST"])
def verify():
    user_otp = request.form.get("otp")
    if user_otp == session.get("otp"):
        session["authenticated"] = True
        return "Login Successful!"
    return "Invalid OTP"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if not session.get("authenticated"):
        return jsonify({"answer": "Please log in with OTP first."})
    user_msg = request.form["message"]
    if contains_bad_language(user_msg):
        return jsonify({"answer": "⚠️ Please avoid inappropriate language."})
    answer = get_response(user_msg)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
