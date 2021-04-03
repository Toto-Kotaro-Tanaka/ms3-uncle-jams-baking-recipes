## TESTING
### Html
— **Code Validation** —

As the core HTML code is completed on all html files, a code validation test is carried out by using [W3C Markup Validation Service](https://validator.w3.org/), which is a validator by the World Wide Web Consortium that allows checking HTML and XHTML documents for well-formed markup, to check any warnings and errors. Flask Jinja template is being used on all html files, source code is being taken from rendered pages.

**Home Page** &#40;`index.html`&#41;: [2 Errors & 4 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-home.png)

1. Error: `<span>` in `<ul>` context<br>
Solve the error by replacing `<span>` by `<li>`

2. Error: `<a>` must not appear as descendant of `<button>`<br>
Solve the error by replacing `<button>` by `<div>`

3. Warning: Section lacks heading<br>
Solve the warning by removing `<section>`

4. Warning: Section lacks heading<br>
Solve the warning by replacing `<section>` by `<div>`

5. Warning: Type attribute unnecessary for JavaScript<br>
Solve the warning by removing it

6. Warning: Type attribute unnecessary for JavaScript<br>
Same as No 5

**Categories Page** &#40;`categories.html`&#41;: 0 Error & 0 Warning

**Recipe Page** &#40;`recipe.html`&#41;: 0 Error & 0 Warning

**Shop Page** &#40;`shop.html`&#41;: [6 Errors & 6 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-shop.png) *Same error and warning on other affiliate images 

1. Error: `<img>` must have an `alt` attribute<br>
Solve the error by putting alt

2. Warning: Border attribute is obsolete<br>
Solve the warning by removing it

**Register Page** &#40;`register.html`&#41;: [0 Error & 1 Warning](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-register.png)

1. Warning: Section lacks heading<br>
Solve the warning by replacing `<section>` by `<div>`

**Login Page** &#40;`login.html`&#41;: 0 Error & 0 Warning

**Profile Page** &#40;`profile.html`&#41;: [5 Errors & 5 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-profile.png) *Same error and warning by 4 times 

1. Error: Duplicate ID<br>
Solve the error by [setting up a unique id](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-profile-id.png) by using Jinja template looping

2. Warning: The first occurrence of ID was here<br>
Same as No 1

**Create Recipe Page** &#40;`create_recipe.html`&#41;: [5 Errors & 1 Warning: 1 & 2](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-create-recipe-1.png) &#47; [5 Errors & 1 Warning: 3 - 6](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-create-recipe-2.png)

1. Error: Attribute required not allowed on element option at this point<br>
Solve the error by removing required attribute. This field is mandatory however Select Category can be selected as an option, because form validator does not prevent this from happening so Other is put as a value. Users selects something on this field so required attribute is not required here

2. Error: Attribute required not allowed on element option at this point<br>
Same as No 1

3. Error: Attribute required not allowed on element option at this point<br>
Same as No 1

4. Warning: Section lacks heading<br>
Solve the warning by replacing `<section>` by `<div>`

5. Error: For attribute of label element must be ID of non-hidden form control
Solve the error by putting ID on input

6. Error: For attribute of label element must be ID of non-hidden form control
Same as No 5

**Edit Recipe Page** &#40;`edit_recipe.html`&#41;: 5 Errors & 1 Warning *Same as Create Recipe<br>
This time, some data is retrieved from the database and they are shown on recipe_ingreds and recipe_steps fiedls with duplicated id. To make unique id, [loop index](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-edit-recipe-id.png) and add on for attribute and id.

**Manage Category Page** &#40;`manage_category.html`&#41;: 0 Error & 0 Warning

**Create Category Page** &#40;`create_category.html`&#41;: 0 Error & 0 Warning

**Edit Category Page** &#40;`edit_category.html`&#41;: 0 Error & 0 Warning


### Css
— **Code Validation** —

### JavaScript
— **Code Validation** —

### Python
— **Initial Function** —

As an initial functions in Python is created, a manual test is carried out.

* Set up *app.py* file and test it by creating `test function` to see if "This is testing" message appears on the page

[Test Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-function.png) / 
[Test Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-function-result.png) &#40;The message is displayed so the function works properly&#41;

— **Connection with Database** —

The connection between the App and MongoDB Atlas is set up so a manual test is carried out.

* `render_template` function is imported to render HTML document when the function is run. A variable called *recipes* is created to retrieve the data from *recipes collection*. Each data in *recipes collection* is retrieved by using Jinja templating language on `index.html`
 
[Connecting Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-connection.png) / [Data in Database](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-db.png) / 
[Connecting Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-connection-result.png) &#40;All the data in recipes collection is displayed so the App and database are connected properly&#41;

— **Base Template** —

The base template for HTML is created so a test is carried out.

* Create `base.html` that contains all main references to external files and third-party libraries for CSS and JavaScript that are used across the entire website.  Block keyword is required to show the contents of child documents
 
[Base Template](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-base-template.png) / 
[Base Template Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-base-template-result.png) &#40;All the contents of parent and child documents are displayed so the base template works properly&#41;

— **Register Function & Form** —

Register function and form are created so a test is carried out.

* Create `register.html` that contains a form to store first time user in *users collection* in *baking_recipe* database to create a unique account. Create a function in `app.py` with POST method with a condition for any usernames, which are not in the database, to be stored in the database. If users already exist in the data, users are led back to register page with a notification.
 
[Register Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register.png) / [Register Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-form.png) / 
[Register Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-result.png) / [Register Failure](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-failure.png) &#40;If there is no username exists in the database, the function stores username & password and if there is, it leads back to register page so the function and the form works properly&#41;

— **Login, Logout Function & Form** —

Login function and form are created so a test is carried out.

* Create `login.html` that contains a form, which takes a username and password. If username and password match with the data in the database, users are led to *Profile* page where they have an option to create and post a recipe as well as to see all of their recipes and Edit and Delete. Create a function in `app.py` with POST method and the function checks both input and the data in the database for authentification. If username and / or password is incorrect, users are led back to login page with a notification.

Logout function is created in `app.py` that when users logout, it removes *session* so they do not see a link to *Profile* page and they cannot even access the page by putting `profile/<username>` on URL.

[Login Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login.png) / [Login Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-form.png) / 
[Login Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-result.png) / [Login Failure](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-failure.png) &#40;When username and password match, users successfully login and when it doesn't it fails so the function and the form works properly&#41;

— **Create Recipe Function & Form** —

Create Recipe function and form are created so a test is carried out.

* Create `create_recipe.html` that contains a form, which takes some user input by a dropdown, input and textarea fields. Create a function in `app.py` with POST method that stores all the input data in the database. There are two data fields, Recipe Ingredients and Steps that take various fields depending on users so this data is stored as Array in the database. Username and posted date, which are not user input, are also stored in the database. 

[Create Recipe Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe.png) / [Create Recipe Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-form.png) / 
[Create Recipe Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-result.png) / [Create Recipe Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-result-data.png) &#40;All the input as well as username and posted date are shown on recipe summary and stored in the database so it works properly&#41;

— **Edit & Delete Recipe Function & Form** —

Edit Recipe function & form and Delete function are created.
Edit recipe function & form work almost the same way as Create Recipe but uses `updated()` method instead of `insert_one()`. 

Delete function uses `remove()` methods to remove the data from the database.

[Edit Recipe Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe.png) / [Edit Recipe Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-form.png) / 
[Edit Recipe Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-result.png) / [Edit Recipe Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-result-data.png) &#40;All updates on the form are updated in the database in the database so it works properly&#41;

— **Manage Category with Create, Edit & Delete Functions & Form** —

Manage Category page with Create, Edit & Delete Functions & Form are created so a test is carried out.

* These work almost the same as Create, Edit and Delete recipes. Create `manage_category.html`, `create_category.html` and `edit_category.html` and functions on app.py. Only admin user has an access to Manage Category page where admin user can create, edit and delete category. To prevent other users to visit Manage Category Page, the link to this page only appears for admin user. This is set up by using if condition on base template. In case users figure out the URL for Manage, Create and Edit category pages, they do not have access to those pages as it is also prevented by if conditions on app.py. 

[Manage Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category.png) / [Manage Category Navbar](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-navbar.png) / [Manage Category Navbar Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-navbar.png) / [Manage Category Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-admin.png) / [Manage Category Non-Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-non-admin.png) &#40;Link to Manage Category page only appears for admin user so it works properly. `manage_category`, `create_category`, `edit_category` URLs are also put in non-admin user and they do not work for non-admin users&#41;

[Create Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category.png) / [Create Category Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-form.png) / 
[Create Category Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-result.png) / [Create Category Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-result-data.png) &#40;A new category is created as expected so it works properly&#41;

[Edit Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category.png) / [Edit Category Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-form.png) / 
[Edit Category Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-result.png) / [Edit Category Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-result-data.png) &#40;Category is edited as expected so it works properly&#41;

— **Search Function and Form** —

Search function and form are created so a test is carried out.

* Create Text index using Python interpreter in the command-line.
Only one Text index can be created on a collection and the purpose of this function is to search recipes by a keyword &#40;s&#41; so text index includes `recipe_title`, `recipe_desc` and `username`. Other documents are excluded from Text Index as there would be too many unnecessary results if we included them. Then, create search function on `app.py` that searches contents in the text index.

[Text Index](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-text-index.png) / [Test Search Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search.png)

[Search By A Word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word.png) / [Search By A Word Result - One recipe contains the word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-result.png)

[Search By A Word 2](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-2.png) / [Search By A Word 2 Result - Two recipes contain the word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-2-result.png)

[Search By Words](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-words.png) / [Search By Words Result - Two recipes contain one of the words](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-words-result.png)

&#40;All the search results came as expected so it works properly&#41;

— **Subscribe To Newsletter Function and Form** —

Subscribe To Newsletter function and form are created so a test is carried out.

* Create `subscribe_newsletter function` on `app.py` with POST method that takes an input email address and stores in the database. 

[Subscribe To Newsletter Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe.png) / [Subscribe To Newsletter Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-form.png) /
[Subscribe To Newsletter Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-result.png) / [Subscribe To Newsletter Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-result-data.png) &#40;Input emails are stored in the database so it works properly&#41;

### Web Browser

### UX