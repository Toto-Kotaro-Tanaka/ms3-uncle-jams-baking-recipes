# Import Python Modules
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from datetime import datetime
if os.path.exists("env.py"):
    import env

# Instance of Flask
app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# MongoDB Global Variable
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    """ To display all recipes by posted date """
    recipes = mongo.db.recipes.find().sort("posted_date", -1)
    categories = mongo.db.categories.find()
    return render_template("index.html", recipes=recipes,
                           categories=categories, search=True)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search by a key word(s) function.  Index is recipe descriptions,\
    recipe title and usrname in recipes collection """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("index.html", recipes=recipes, search=True)


@app.route("/categories/<category_name>")
def categories(category_name):
    """ To display recipes by category by posted date """
    recipes = mongo.db.recipes.find(
        {"category_name": category_name}).sort("posted_date", -1)
    categories = mongo.db.categories.find()
    return render_template("categories.html",
                           recipes=recipes, category_name=category_name,
                           categories=categories, title=category_name,
                           search=True)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """ To display an individual recipe """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html",
                           recipe=recipe, recipe_title=recipe,
                           hide_navbar_footer=True)


@app.route("/shop")
def shop():
    """ To display all baking tools available to buy """
    categories = mongo.db.categories.find()
    return render_template("shop.html", categories=categories, title="Shop")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ To create an account to create, post, edit and delete recipes """
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

    return render_template("register.html", title="Register",
                           hide_navbar_footer=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    """ To login the webiste """
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
    """ User profile where users have access to all their recipes,\
         and to create, edit and delete recipes """
    recipes = mongo.db.recipes.find().sort("posted_date", -1)
    categories = mongo.db.categories.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", recipes=recipes,
                               categories=categories, username=username,
                               title=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Logout function """
    flash("You have logged out", "success")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    # Prevent none user accessing this page
    """ To create recipes """
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

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_recipe.html",
                           categories=categories, title="Create Recipe",
                           hide_navbar_footer=True, jquery=True)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """ To edit recipes. Users only have access to their\
        own recipes and if users try to access to someone's\
        recipes, they are redirected to home page """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if session["user"].lower() != recipe["username"].lower():
        return redirect(url_for("profile", username=session["user"]))

    else:
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
        categories = mongo.db.categories.find()

        return render_template("edit_recipe.html", recipe=recipe,
                               categories=categories, recipe_title=recipe,
                               hide_navbar_footer=True, jquery=True)

    # return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_recipe/<recipe_id>", methods=["GET", "POST"])
def delete_recipe(recipe_id):
    """ Delete recipes function """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted", "success")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/manage_category")
def manage_category():
    """ To manage categories where only Admin has access to it\
        and access to create, edit category pages and delete function """
    categories = mongo.db.categories.find()
    manage_categories = list(mongo.db.categories.find().sort("_id", -1))

    if session["user"] == "admin":
        return render_template("manage_category.html", categories=categories,
                               manage_categories=manage_categories,
                               title="Manage Category")

    return redirect(url_for("home", username=session["user"]))


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    """ To create categories and only Admin has access to it """
    if session["user"] == "admin":

        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name").lower()
            }
            mongo.db.categories.insert_one(category)
            flash("You have created a new category", "success")
            return redirect(url_for("manage_category"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("create_category.html",
                               categories=categories, title="Create Category",
                               hide_navbar_footer=True, jquery=True)

    # Question: If this is ok or should be redirected page 404 or 401?
    return redirect(url_for("home"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ To edit categories and only Admin has access to it """
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

    # Question: If this is ok or should be redirected page 404 or 401?
    return redirect(url_for("home"))


@app.route("/delete_category/<category_id>", methods=["GET", "POST"])
def delete_category(category_id):
    """ Delete categories function and only Admin has access to it """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category successfully deleted", "success")
    return redirect(url_for("manage_category"))


@app.route("/subscribe_newsletter", methods=["GET", "POST"])
def subscribe_newsletter():
    """ Subscribe newsletter function """
    if request.method == "POST":
        existing_email = mongo.db.emails.find_one(
            {"subsc_email": request.form.get("subsc_email")})

        if existing_email:
            flash("You are already subscribed", "error")
            return redirect(url_for("home"))

        else:  # Do you need esle ?
            email = {
                "subsc_email": request.form.get("subsc_email")
            }
            mongo.db.emails.insert_one(email)
            flash("Thank your for your subscription", "success")
            return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    """ To handle not found page """
    return render_template("page_404.html", title="Page 404",
                           hide_navbar_footer=True), 404


# IP & PORT Environment Variables
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Change this to False before submission of the project and delete this message
