from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:4yuC0tEOO7lyOXJRIVcI@containers-us-west-82.railway.app:6642/")
db = client["sample"]
collection = db["user"]

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/save_user", methods=["POST"])
def save_user():
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    age = request.form.get("age")
    email = request.form.get("email")
    gender = request.form.get("gender")

    user = {
        "name": name,
        "mobile": mobile,
        "age": age,
        "email": email,
        "gender": gender
    }

    collection.insert_one(user)

    return "User saved successfully."

if __name__ == "__main__":
    app.run()
