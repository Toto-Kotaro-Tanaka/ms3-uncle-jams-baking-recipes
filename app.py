import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    recipes = mongo.db.recipes.find().sort("posted_date", -1)
    return render_template("index.html", recipes=recipes, search=True)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("index.html", recipes=recipes, search=True)


@app.route("/categories/<category_name>")
def categories(category_name):
    recipes = mongo.db.recipes.find(
        {"category_name": category_name}).sort("posted_date", -1)
    return render_template("categories.html",
                           recipes=recipes, category_name=category_name,
                           title=category_name, search=True)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html",
                           recipe=recipe, recipe_title=recipe,
                           hide_navbar_footer=True)


@app.route("/shop")
def shop():
    return render_template("shop.html", title="Shop")


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

    return render_template("register.html", title="Register", hide_navbar_footer=True)


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

    return render_template("login.html", title="Login",
                           hide_navbar_footer=True)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    recipes = mongo.db.recipes.find().sort("posted_date", -1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username,
                               recipes=recipes, title=username)

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
                           categories=categories, title="Create Recipe", hide_navbar_footer=True,
                           jquery=True)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
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
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated", "success")
        return redirect(url_for("home"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes = mongo.db.recipes.find_one()  # This can be deleted - check later
    categories = mongo.db.categories.find().sort("category_name")

    return render_template("edit_recipe.html", recipe=recipe, recipes=recipes,
                           categories=categories, recipe_title=recipe,
                           hide_navbar_footer=True, jquery=True)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted", "success")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/manage_category")
def manage_category():
    categories = list(mongo.db.categories.find().sort("_id", -1))

    if session["user"] == "admin":
        return render_template("manage_category.html",
                               categories=categories, title="Manage Category")

    return redirect(url_for("home", username=session["user"]))


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    if session["user"] == "admin":

        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("You have created a new category", "success")
            return redirect(url_for("manage_category"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("create_category.html",
                               categories=categories, title="Create Category",
                               hide_navbar_footer=True, jquery=True)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if session["user"] == "admin":

        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category successfully updated", "success")
            return redirect(url_for("manage_category"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category,
                               title="Edit Category", hide_navbar_footer=True)

    # Question: If this is ok or should be redirected page 404?
    return redirect(url_for("home"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category successfully deleted", "success")
    return redirect(url_for("manage_category"))


@app.route("/subscribe_newsletter", methods=["GET", "POST"])
def subscribe_newsletter():
    if request.method == "POST":
        email = {
            "subsc_email": request.form.get("subsc_email")
        }
        mongo.db.emails.insert_one(email)
        flash("Thank your for your subscription", "success")
        return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_404.html", title="Page 404",
                           hide_navbar_footer=True), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Change this to False before submission of the project and delete this message
