import os
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    recipes = mongo.db.recipes.find().sort("_id", -1)
    return render_template("index.html", recipes=recipes)


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Welcome, {}".format(
            request.form.get("username")), "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", hide_navbar_footer=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(
                    request.form.get("username")), "success")
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username and/or password", "error")
                return redirect(url_for("login"))
        else:
            flash("Incorrect username and/or password", "error")
            return redirect(url_for("login"))

    return render_template("login.html", hide_navbar_footer=True)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have logged out", "success")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_desc": request.form.get("recipe_desc"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_ingreds": request.form.getlist("recipe_ingreds"),
            "recipe_steps": request.form.getlist("recipe_steps"),
            "recipe_img_url": request.form.get("recipe_img_url"),
            "recipe_tips": request.form.get("recipe_tips"),
            "username": session["user"],
            "posted_date": datetime.today().strftime("%d %b, %Y")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("You have posted your recipe", "success")
        return redirect(url_for("home"))

    categories = mongo.db.categories.find().sort("category_name")
    return render_template("create_recipe.html",
                           categories=categories, hide_navbar_footer=True,
                           jquery=True)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Change this to False before submission of the project and delete this message
