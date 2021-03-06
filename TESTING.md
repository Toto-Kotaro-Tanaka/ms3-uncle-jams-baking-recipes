## TESTING <a name="testing-top"></a>

### Html

— **Code Validation** —

As the core HTML code is completed on all HTML files, a code validation test is carried out by using [W3C Markup Validation Service](https://validator.w3.org/), which is a validator by the World Wide Web Consortium that allows checking HTML and XHTML documents for well-formed markup, to check any warnings and errors. As Flask Jinja template is used on all HTML files, source code is taken from rendered pages for the testing.

**Home Page** &#40;`index.html`&#41;: [2 Errors & 4 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-home.png)

1. Error: `<span>` in `<ul>` context<br>
   Solve the error by replacing `<span>` to `<li>`

2. Error: `<a>` must not appear as descendant of `<button>`<br>
   Solve the error by replacing `<button>` to `<div>`

3. Warning: Section lacks heading<br>
   Solve the warning by removing `<section>`

4. Warning: Section lacks heading<br>
   Solve the warning by replacing `<section>` to `<div>`

5. Warning: Type attribute unnecessary for JavaScript<br>
   Solve the warning by removing it

6. Warning: Type attribute unnecessary for JavaScript<br>
   Same as No 5

**Categories Page** &#40;`categories.html`&#41;: 0 Error & 0 Warning

**Recipe Page** &#40;`recipe.html`&#41;: 0 Error & 0 Warning

**Shop Page** &#40;`shop.html`&#41;: [6 Errors & 6 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-shop.png) \*Same error and warning on other affiliate images

1. Error: `<img>` must have an `alt` attribute<br>
   Solve the error by putting alt

2. Warning: Border attribute is obsolete<br>
   Solve the warning by removing it

**Register Page** &#40;`register.html`&#41;: [0 Error & 1 Warning](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-register.png)

1. Warning: Section lacks heading<br>
   Solve the warning by replacing `<section>` to `<div>`

**Login Page** &#40;`login.html`&#41;: 0 Error & 0 Warning

**Profile Page** &#40;`profile.html`&#41;: [5 Errors & 5 Warnings](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-profile.png) \*Same error and warning by 4 more times

1. Error: Duplicate ID<br>
   Solve the error by [setting up a unique id](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-profile-id.png) by using Jinja template looping

2. Warning: The first occurrence of ID was here<br>
   Same as No 1

**Create Recipe Page** &#40;`create_recipe.html`&#41;: [5 Errors & 1 Warning: 1 & 2](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-create-recipe-1.png) &#47; [5 Errors & 1 Warning: 3 - 6](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-create-recipe-2.png)

1. Error: Attribute required not allowed on element option at this point<br>
   Solve the error by removing the required attribute. This field is mandatory however **Select Category** can be selected as an option because the form validator does not prevent this from happening so *Other* is put as a value. Users automatically select something on this field so the required attribute is not required here

2. Error: Attribute required not allowed on element option at this point<br>
   Same as No 1

3. Error: Attribute required not allowed on element option at this point<br>
   Same as No 1

4. Warning: Section lacks heading<br>
   Solve the warning by replacing `<section>` to `<div>`

5. Error: For attribute of label element must be ID of non-hidden form control<br>
   Solve the error by putting ID on the input

6. Error: For attribute of label element must be ID of non-hidden form control<br>
   Same as No 5

**Edit Recipe Page** &#40;`edit_recipe.html`&#41;: 5 Errors & 1 Warning \*Same as Create Recipe<br>

- This time, some data is retrieved from the database and they are shown on *recipe_ingreds* and *recipe_steps* fields with duplicated id. To make a unique id, [loop index](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-code-validation-edit-recipe-id.png) and add on for attribute and id.

**Manage Category Page** &#40;`manage_category.html`&#41;: 0 Error & 0 Warning

**Create Category Page** &#40;`create_category.html`&#41;: 0 Error & 0 Warning

**Edit Category Page** &#40;`edit_category.html`&#41;: 0 Error & 0 Warning

**404 Page** &#40;`page_404.html`&#41;: 0 Error & 0 Warning

---

— **Form Validation** —

All the forms used on the website is validated by HTML. A manual test is carried out to see if those forms are validated properly.

**Register**

- Only the alphabet and numbers can be used as a username, and the length must be between 5 - 15. When invalid letters, including space, there is a warning message pops up. For password, any letters can be used but must be 5 or more letters so a warning message pops up for an invalid length. If the user already exists in the system, then an error message pops up saying **User already exists** and it will not process the registration

**Login**

- Username and password must match to log in. If one of them or both are incorrect, an error message pops up saying **Incorrect username and/or password**. Not saying what is incorrec is important because this is to make more difficult for brute-forcing an account

**Create & Edit Recipe &#40;Category&#41;**

- All the fields except Recipe Image URL and Tips are mandatory. Unless users select something on the fields, it gives an error. If Recipe Image URL is empty, then, it creates a default image for the recipe. There is an issue on Create Recipe form that the title of the dropdown menu can be selected even if it is set to disable. An empty entry for the category causes an issue so put `value="other"` for this. &#40;Same ideas for Recipe Time and Serves&#41; For Recipe Ingredients and steps, fields can be added and they cannot be submitted as empty fields

**Subscribe to our newsletter**

- Input email must contain &#64; mark and some letters after. Otherwise, an error message pops up. If the email already exists in the system, then an error message pops up saying **Email already exists** and it will not process the subscription

---

— **Quality** —

As the core HTML code is completed, a quality check test is carried out by using [Lighthouse](https://developers.google.com/web/tools/lighthouse), which is an open-source and one of the automated DevTools for improving the quality of web pages. It has audits for performance, accessibility, progressive web apps, SEO.

**Home Page** &#40;`index.html`&#41;

- Mobile Size: [Performance: 61 / Accessibility: 90 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-home-mobile.png)

- Desktop Size: [Performance: 93 / Accessibility: 90 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-home-desktop.png)

**Categories Page** &#40;`categories.html`&#41;

- Mobile Size: [Performance: 57 / Accessibility: 90 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-categories-mobile.png)

- Desktop Size: [Performance: 94 / Accessibility: 90 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-categories-desktop.png)

**Recipe Page** &#40;`recipe.html`&#41;

- Mobile Size: [Performance: 76 / Accessibility: 96 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-recipe-mobile.png)

- Desktop Size: [Performance: 99 / Accessibility: 96 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-recipe-desktop.png)

**Shop Page** &#40;`shop.html`&#41;

- Mobile Size: [Performance: 66 / Accessibility: 90 / Best Practices: 86 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-shop-mobile.png)

- Desktop Size: [Performance: 95 / Accessibility: 90 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-shop-desktop.png)

**Register Page** &#40;`register.html`&#41;

- Mobile Size: [Performance: 66 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-register-mobile.png)

- Desktop Size: [Performance: 100 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-register-desktop.png)

**Login Page** &#40;`login.html`&#41;

- Mobile Size: [Performance: 91 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-login-mobile.png)

- Desktop Size: [Performance: 99 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-login-desktop.png)

**Profile Page** &#40;`profile.html`&#41;

- Mobile Size: [Performance: 75 / Accessibility: 91 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-profile-mobile.png)

- Desktop Size: [Performance: 100 / Accessibility: 91 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-profile-desktop.png)

**Create Recipe Page** &#40;`create_recipe.html`&#41;

- Mobile Size: [Performance: 85 / Accessibility: 100 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-create-recipe-mobile.png)

- Desktop Size: [Performance: 99 / Accessibility: 100 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-create-recipe-desktop.png)

**Edit Recipe Page** &#40;`edit_recipe.html`&#41;

- Mobile Size: [Performance: 82 / Accessibility: 100 / Best Practices: 93 / SEO: 92](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-edit-recipe-mobile.png)

- Desktop Size: [Performance: 98 / Accessibility: 100 / Best Practices: 93 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-edit-recipe-desktop.png)

**Manage Category Page** &#40;`manage_category.html`&#41;

- Mobile Size: [Performance: 71 / Accessibility: 90 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-manage-category-mobile.png)

- Desktop Size: [Performance: 96 / Accessibility: 90 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-manage-category-desktop.png)

**Create Category Page** &#40;`create_category.html`&#41;

- Mobile Size: [Performance: 78 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-create-category-mobile.png)

- Desktop Size: [Performance: 99 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-create-category-desktop.png)

**Edit Category Page** &#40;`edit_category.html`&#41;

- Mobile Size: [Performance: 83 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-edit-category-mobile.png)

- Desktop Size: [Performance: 100 / Accessibility: 100 / Best Practices: 100 / SEO: 100](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-edit-category-desktop.png)

> Address the **low performance on mobile size** and try to improve it as much as possible. Examine the issues by the reports on Lighthouse on `index.html` which must be the same or similar issues causing on other HTML files. Two main issues of the low performance are caused by [Eliminate render-blocking resources and Serve images in next-gen formats](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-two-main-issues.png). 
>
> **Eliminate render-blocking resources:**
> - According to [coverage](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-coverage.png) by Google DevTools, this is caused by *MDB (Material Design Bootstrap) CDNs*. Look for solutions on the internet however, this seems to be [beyond my current ability](https://mdbootstrap.com/support/jquery/unused-css-and-javascript-page-performance/) so decide to leave as it is
>
> **Serve images in next-gen formats:**
> - Try to use JPG2000 format as per [web.dev's suggestion](https://web.dev/uses-webp-images/?utm_source=lighthouse&utm_medium=devtools), however, there are some other issues. JP2 format is not recognised for some reason so images do not show. Try to use JPG instead but my images are transparent and it cannot be used in JPG format so decide to keep all images as they are
>
> There are two more issues that could improve the performance. These are [Image elements do not have explicit width and height & Serve static assets with an efficient cache policy](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-two-issues.png). 
>
> **Image elements do not have explicit width and height**
> - Try to fix as per [dev.web's suggestion](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/html/test-quality-width-height.png) however, not only this does not improve the performance but also this causes issues on *Best Practice* so decide to leave as they are
>
> **Serve static assets with an efficient cache policy**
> - This seems to be [beyond my current ability](https://web.dev/uses-long-cache-ttl/#:~:text=When%20a%20browser%20requests%20a,getting%20it%20from%20the%20network) so decide to leave it as it is

<div align="right"><a href="#testing-top">🔝</a></div>

---

### Css

— **Code Validation** —

As the core CSS code is completed, a code validation test is carried out by using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), which is a validator by the World Wide Web Consortium that allows checking Cascading Style Sheets, to make sure that CSS complies with the standards set by the World Wide Web Consortium

**`style.css`**: [0 Error & 1 Warning](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/css/test-style.png)

- 1 warning is related to WebKit, which is one of [web browser rendering engines](https://stackoverflow.com/questions/3468154/what-is-webkit-and-how-is-it-related-to-css). By looking at the [Stack Overflow](https://stackoverflow.com/questions/52490004/what-are-all-of-these-w3c-css-validation-warnings-about) post and a [Code Institue Slack](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/css/webkit.png) threads, no further actions are required so decide to leave as it is

---

### JavaScript

— **Code Validation** —

As the core JavaScript code is completed, a code validation test is carried out by using [JSHint](https://jshint.com/), which is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules

**`script.js`**: [1 Unused Variable](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/js/test-script.png)

- This is just a function that is controlled on click so can be ignored

**`createRecipe.js`**: [2 Warnings & 1 Unused Variable](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/js/test-createRecipe.png)

- 2 warnings are fixed by putting semicolon and &#36; is jQuery symbol so can be ignored

---

### Python

— **Functions** —

**Initial Function:** As an initial function in Python is created, a test is carried out.

- Set up *app.py* file and test it by creating `test function` to see if "This is testing" message appears on the page<br>
[Test Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-function.png) / [Test Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-function-result.png) &#40;The message is displayed so the function works properly&#41;

**Connection with Database:** The connection between the App and MongoDB Atlas is set up so a test is carried out.

- `render_template` function is imported to render HTML document when the function is run. A variable called *recipes* is created to retrieve the data from *recipes collection*. Each data in *recipes collection* is retrieved by using Jinja templating language on `index.html`<br>
[Connecting Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-connection.png) / [Data in Database](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-db.png) / [Connecting Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-db-connection-result.png) &#40;All the data in recipes collection is displayed so the App and database are connected properly&#41;

**Base Template:** The base template for HTML is created so a test is carried out.

- Create `base.html` that contains all main references to external files and third-party libraries for CSS and JavaScript that are used across the entire website. Block keyword is required to show the contents of child documents<br>
[Base Template](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-base-template.png) / [Base Template Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-base-template-result.png) &#40;All the contents of parent and child documents are displayed so the base template works properly&#41;

**Register Function & Form:** Register function and form are created so a test is carried out.

- Create `register.html` that contains a form to store first time user in *users collection* in *baking_recipe* database to create a unique account. Create a function in `app.py` with POST method with a condition for any usernames, which are not in the database, to be stored in the database. If users already exist in the data, users are led back to *Register* page with a notification.<br>
[Register Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register.png) / [Register Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-form.png) / [Register Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-result.png) / [Register Failure](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-register-failure.png) &#40;If there is no username exists in the database, the function stores username & password and if there is, it leads back to *Register* page so the function and the form works properly&#41;

**Login, Logout Function & Form:** Login function and form are created so a test is carried out.

- Create `login.html` that contains a form, which takes a username and password. If username and password match with the data in the database, users are led to *Profile* page where they have an option to create and post a recipe as well as to see all of their recipes with Edit and Delete functions. Create a function in `app.py` with POST method and the function checks both input and the data in the database for authentification. If username and&#47;or password is incorrect, users are led back to *Login* page with a notification.<br>
Logout function is created in `app.py` that when users logout, it removes *session* so they do not see a link to *Profile* page and they cannot even access the page by putting `profile/<username>` on URL.<br>
[Login Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login.png) / [Login Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-form.png) / [Login Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-result.png) / [Login Failure](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-login-failure.png) &#40;When username and password match, users successfully log in and when it does not it fails so the function and the form works properly&#41;

**Create Recipe Function & Form:** Create Recipe function and form are created so a test is carried out.

- Create `create_recipe.html` that contains a form, which takes some user input by a dropdown, input and textarea fields. Create a function in `app.py` with POST method that stores all the input data in the database. There are two data fields, Recipe Ingredients and Steps that take various fields depending on users so this data is stored as Array in the database. Username and posted date, which are not user input, are also stored in the database.<br>
[Create Recipe Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe.png) / [Create Recipe Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-form.png) / [Create Recipe Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-result.png) / [Create Recipe Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-recipe-result-data.png) &#40;All the input as well as username and posted date are shown on recipe summary and stored in the database so it works properly&#41;

**Edit & Delete Recipe Function & Form:** Edit Recipe function & form and Delete function are created so a test is carried out.

- Edit recipe function & form work almost the same way as Create Recipe but uses `updated()` method instead of `insert_one()`.<br>
Delete function uses `remove()` methods to remove the data from the database.<br>
[Edit Recipe Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe.png) / [Edit Recipe Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-form.png) / [Edit Recipe Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-result.png) / [Edit Recipe Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-recipe-result-data.png) &#40;All updates on the form are updated in the database so it works properly&#41;

**Manage Category with Create, Edit & Delete Functions & Form:** Manage Category page with Create, Edit & Delete Functions & Form are created so a test is carried out.

- These work almost the same as Create, Edit and Delete recipes. Create `manage_category.html`, `create_category.html` and `edit_category.html` and functions on app.py. Only admin user has an access to *Manage Category* page where admin user can create, edit and delete category. To prevent other users from visiting *Manage Category* Page, the link to this page only appears for admin user. This is set up by using `if condition` on base template. In case users figure out the URL for Manage, Create and Edit category pages, they do not have access to those pages as it is also prevented by `if conditions` on `app.py`.<br>
[Manage Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category.png) / [Manage Category Navbar Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-navbar-admin.png) / [Manage Category Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-admin.png) / [Manage Category Non-Admin](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-manage-category-non-admin.png) &#40;Link to Manage Category page only appears for admin user so it works properly. `manage_category`, `create_category`, `edit_category` URLs are also put in non-admin user for testing and they do not work for non-admin users&#41;<br>
[Create Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category.png) / [Create Category Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-form.png) /
[Create Category Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-result.png) / [Create Category Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-create-category-result-data.png) &#40;A new category is created as expected so it works properly&#41;<br>
[Edit Category Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category.png) / [Edit Category Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-form.png) / [Edit Category Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-result.png) / [Edit Category Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-edit-category-result-data.png) &#40;Category is edited as expected so it works properly&#41;

**Search Function and Form:** Search function and form are created so a test is carried out.

- Create Text index using Python interpreter on the command-line. Only one Text index can be created on a collection and the purpose of this function is to search recipes by a keyword&#40;s&#41; so text index includes `recipe_title`, `recipe_desc` and `username`. Other documents are excluded from Text Index as there would be too many unnecessary results if these are included. Then, create a search function on `app.py` that searches contents in the text index.<br>
[Text Index](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-text-index.png) / [Test Search Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search.png)<br>
[Search By A Word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word.png) / [Search By A Word Result - One recipe contains the word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-result.png)<br>
[Search By A Word 2](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-2.png) / [Search By A Word 2 Result - Two recipes contain the word](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-word-2-result.png)<br>
[Search By Words](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-words.png) / [Search By Words Result - Two recipes contain one of the words](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-search-words-result.png)<br>
  &#40;All the search results came as expected so it works properly&#41;

**Subscribe To Newsletter Function and Form:** Subscribe To Newsletter function and form are created so a test is carried out.

- Create `subscribe_newsletter function` on `app.py` with POST method that takes an input email address and stores it in the database.<br>
[Subscribe To Newsletter Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe.png) / [Subscribe To Newsletter Form](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-form.png) /
[Subscribe To Newsletter Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-result.png) / [Subscribe To Newsletter Result Data](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-subscribe-result-data.png) &#40;Input emails are stored in the database so it works properly&#41;

---

— **Code Validation** —

As Python code is completed on `app.py`, a code validation test is carried out by using [PEP8 &#40;Python Enhancement Proposal&#41; online](http://pep8online.com) to see if the code meets guidelines and best practices for the readability and consistency of Python code.

**`app.py`**: [All right](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/python/test-pep8.png)

---

### Defensive Programme

There are some pages on the website that users without permission are not allowed to access. Interface prevents those users who have no permission from accessing these pages &#40;i.e Create recipe page can be accessed from Profile page where only users who log in have access by navigation bar&#41;, however, by typing URL, non-authorised users can try to access these pages so there are some defensive programmes set up to prevent this from happening. 

Below are the tests and results to check to see if the defensive programmes work properly.

**Non-Logged in users who;**

- try to access *Profile* page are led to *Error 404*. If they type `profile/<actual username>`, then they are led to *Register* page with "Access denied. Create your own account and login" message
- try to access *Create Recipe* page are led to *Register* page with "Access denied. Create your own account and login" message
- try to access *Edit Recipe* page are led to *Error 404*. If they type `edit_recipe/<object id>`, they are led to *Register* page with "Access denied. This is not your recipe" message
- try to access *Delete Recipe* function by typing `delete/<object id>` are led to *Register* page with "Access denied. This is not your recipe" message

> **Note:**<br>
> Same&#47;similar things happen when Non-Logged in uses try to access *Manage Category*, *Create Category*, *Edit Category* pages and *Delete Category* function.

**Logged in users who;**

- try to access someone's recipe by typing `edit_recipe/<object id>` and `delete_recipe/<object id>` are led to *Profile* page with "Access denied. This is not your recipe" message
- are NOT Admin and try to access *Manage Category*, *Create Category*, *Edit Category* pages and *Delete Category* function are led to *Profile* page with "Access denied. You don't have permission" message

---

### Web Browser

— **Visibilities and CRUD functionality** —

The website is available on the major web browsers, such as **Chrome**, **Safari**, **Firefox**, **Opera** and **Microsoft Edge**. To make sure all the visual contents are shown and functions work properly on those browsers, the below tests are carried out on all of them. *Except Chrom that is used to build the website

1. Open the website on the browser to do a visual test. Look at all the pages to see if everything appears as expected
2. Create a user and test CRUD functions
   - Create a recipe and post it
   - Check to see if they appear on Home page and Categories page
   - Edit a recipe
   - Create another recipe and delete it
   - Subscribe newsletter

> All the above functions work without any problem on each browser

---

### UX

— **Evidence Of Achieving The Website From UX Point Of View** —

There are some key features to achieve the primary goals of the website from user's point of view and this is to confirm that these features are on the website for both visually and functionality.

- A page where users can see a summary of all the recipes
- A page where users can see recipes by category
- A page where users can see a full recipe
- A page where users can buy some baking items &#40;Owner gets a commission by selling items on the website and it is owner's primary goal&#41;
- A page and function to create an account and login for those who would like to share their recipes
- A page where users can see only their recipes
- A page and function to create and post recipes with simple steps
- A page and function to edit and delete recipes
- A function to search specific recipes by a keyword&#40;s&#41;
- A function to subscribe newsletter

> Everything outlined above is implemented on the website and works properly

---

### Unsolved Issues
There are a few issues in the project that are addressed to get them solved however they remain unsolved issues due to a lack of my current skill and&#47;or time

**Low Performance on Mobile Size**

- Try to improve it but cannot do it because of my current skillset and time. Hope to have the skillset in the near future as I continue learning 

**3 Errors on Console**

- There is [an error on create_recipe](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-console-create-recipe.png) and [errors on edit_recipe](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-console_edit_recipe.png) HTML files. These errors are related to Material Design Bootstrap that I cannot do anything with. These errors do not cause any issues on the website so they are left as they are 

**Recipe Ingredients & Steps on edit_recipe.html**

- To solve the issue by W3C Markup Validation Service for HTML code, [loop is set up](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-label.png) for `for attribute` of label for Recipe Ingredients and Steps, so that it corresponds to a unique ID of the input field. However, this causes an issue of [showing the label multiple times](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-repeat-label.png) on *Edit Recipe*. Try to think of showing only one label but cannot solve it and also this is *Edit Recipe* page where users have some ideas of what inputs are so decide to leave the [label empty](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-empty-label.png)

> **Note**<br>
> Initially, it loops through to have [a label for each input box](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-label-input.png). This works from HTML code validation's point of view however, when click add more ingredients button, it [adds a new input box underneath each existing input box](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-label-duplicate-input.png) instead of adding just one so this is not a solution either

**Edit Recipe to Remove Ingredients and Steps**

- On *Edit Recipe* page, a new input field can be added and deleted, [existing fields](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/testing/unsolved-issues/test-input-delete.png) can be edited but cannot be deleted. This is not a major function issue so leave it as it is as no time to look deep into the issue

<div align="right"><a href="#testing-top">🔝</a></div>