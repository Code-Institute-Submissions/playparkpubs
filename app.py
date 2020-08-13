import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    most_recent = mongo.db.reviews.find().limit(10).sort("_id", -1)
    top_ten = mongo.db.reviews.find().limit(5).sort("total_score", -1)
    return render_template("index.html", most_recent=most_recent, top_ten=top_ten)

@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find().sort("_id", -1)
    return render_template("reviews.html", reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")), debug=True)