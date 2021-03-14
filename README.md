<!--- Logo goes here --->
# [Uncle Jam's Baking Recipes] <!--- Link of the website goes here --->
This is a website for baking recipes of bread, cakes, and biscuits. I create this for **Milestone Project 3 (Python and Data Centric Development), Full Stack Software Development** in [Code Institute](https://codeinstitute.net/), Ireland.
It is a mobile responsive website and the link to the website is available HERE. <!--- Link of the website goes here --->

<!--- Mockup goes here --->

## TABLE OF CONTENTS <a name="table-of-contents"></a>
* #### [WHO'S THIS WEBSITE FOR?](#whos-this-website-for-heading)
* #### [WHO IS THE OWNER?](#who-is-the-owner-heading)
* #### [UX 5 PLANES](#ux5-planes-heading)
    * ##### [Strategy Plane](#strategy-plane-heading)
    * ##### [Scope Plane](#scope-plane-heading)
    * ##### [Structure Plane](#structure-plane-heading)
    * ##### [Skeleton Plane](#skeleton-plane-heading)
    * ##### [Surface Plane](#surface-plane-heading)
* #### [WEBSITE CONSTRUCTION PLANS](#website-construction-plans-heading)
* #### [TECHNOLOGIES USED](#technologies-used-heading)
* #### [TESTING](#testing-heading)
    * ##### [Python](#python-heading)
* #### [PROJECT BARRIERS & SOLUTIONS](#barriers-solutions-heading)
* #### [DEPLOYMENT](#deployment-heading)

## WHO'S THIS WEBSITE FOR? <a name="whos-this-website-for-heading"></a>
This is a website for people who simply love baking, or even just beginning to be interested in baking. People who would like to see someone’s recipes for new ideas and / or who would like to share their own recipes with other people can do both on this website. The website is designed to be obvious its purpose for first-time users. Everything is laid out simply and navigated quite easily so users can adapt to the website fairly quickly, and that makes users keep coming back to the website. All the recipes are visible to any users so they do not need to create an account if they just would like to see recipes. If users would like to post their recipes, then they need to create an account but the process of creating an account is very simple. Some users may want to buy new baking items so there is a *Shop* page that uses can look at some items and purchase them on the seller's website. There is a section to subscribe newsletters to get engaged informed what’s happening in baking and community.

<div align="right"><a href="#table-of-contents">🔝</a></div>

## WHO IS THE OWNER? <a name="who-is-the-owner-heading"></a>
I am the owner of the website. The primary goal of the website is to provide a platform that users can see baking recipes and / or share their recipes without any hassles. There is a *Shop* page that some baking items are listed &#40;affiliate&#41; so in case users find something interesting, they can access to the seller's website for more details of the items and can also purchase them. I can get a commission from the seller for any items being sold through my website and this is also one of the goals. I would like to collect their e-mail address for newsletters to expand the community.

<div align="right"><a href="#table-of-contents">🔝</a></div>

## UX 5 PLANES <a name="ux5-planes-heading"></a>

### Strategy Plane <a name="strategy-plane-heading"></a>

The website is designed for those who love baking, and who are interested in baking. People who have been baking might want to share their knowledge with other people as it gives them great feeling and motivation, so by following very simple registration steps, they can create an account and post their recipes in a well-structured format. People who have less experience in baking and would just like to see recipes, they can do it simply by visiting the website, where all the recipes are shown by posted date, or they can see them by category &#40;bread, cake, biscuit&#41; on different pages. There is a search field on the website so they can search for specific recipes by keywords. To see recipes, users do not need to register so it is hassle-free. There is a *shop* page that has a number of baking items in an affiliate style so in case users would like to purchase something, they can do it by clicking the link and it leads users to the website of the sellers. The design of the website is meaningful and simple so that the purpose of the website is very clear for first-time users, and they can easily adapt to the website, and this also applies to all the functions to create, post, edit and delet recipes for regular users. Owner’s main goal is to provide a community platform that is easy to use whether they are first-time or returning users, and this is the key to grow the community. To achieve this, the website is designed and created by user first concept.

All the functions on the tables below are minimum requirements on the website to achieve the current user's and owner's goals. &#40;On a scale of 1 &#91;least&#93; - 5 &#91;most&#93;&#41;

| Opportunity                                 | Importance | Viability / Feasibility |
| :------------------------------------------ | :--------: | :---------------------: |
| Register                                    |     5      |            5            |
| Login / Log out                             |     5      |            5            |
| Post / Edit / Delete Recipes                |     5      |            4            |
| Search Recipes By Keywords                  |     4      |            5            |
| Show Recipes By Category                    |     4      |            5            |
| Shop &#40;Affiliate&#41;                    |     4      |            5            |
| Responsiveness                              |     4      |            5            |
| Subscribe To Newsletter                     |     4      |            4            |
| Manage Recipe Category &#40;Admin only&#41; |     3      |            5            |
| Page 404                                    |     3      |            4            |

Below are the additional functions that can improve the website, however, these are not mandatory to achieve the current user's and owner's goals. Some are not implemented due to a lack of my current skills & knowledge and some due to a lack of time.

| Opportunity                             | Importance | Viability / Feasibility |
| :-------------------------------------- | :--------: | :---------------------: |
| Resetting Password When Users Forget It |     4      |            2            |
| Upload Image For Each Recipe            |     4      |            2            |
| Pagination                              |     3      |            3            |
| Review By Other Users                   |     3      |            3            |
| “Like” Reaction By Other Users          |     3      |            2            |

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Scope Plane <a name="scope-plane-heading"></a>
To achieve user and owner’s goals, below are the minimum features to be included in this project. Also, CRUD &#40;Create, Read, Update, and Delete&#41; functions are required for this project so these are implemented as a part of essential features. 
* Simple design Home page that first-time users can recognise the purpose of the website easily. All the recipes are shown on *Home* page &#40;R&#41;
* Categories &#40;Bread, Cake and Biscuit&#41; pages that users can see recipes by the categories &#40;R&#41;
* Shop page that users can see some baking items, which are linked to the seller’s website
* Register page that users can create an account to post and edit recipes
* Login page that users can log in to the website
* Logout function that users can log out
* Profile page that users can see all their recipes and access to create, edit and delete recipes 
* Create Recipe page that users can create their recipes and post them &#40;C&#41;
* Edit Recipe page that users can edit their recipes &#40;U&#41;
* Delete Recipe function that users can delete their recipes &#40;D&#41;
* Manage Category functions that only <ins>admin user</ins> &#40;owner&#41; can create, edit and delete categories &#40;C & U & D&#41;
* Search by keywords function that users can search for specific recipes
* Subscribe to newsletter section to collect users email addresses
* 404 page that takes users back to *Home* page of the website safely  

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Structure Plane <a name="structure-plane-heading"></a>

— Front-end —<br>
The website consists of **Home** page with **14 other core pages**.
* **Home** &#40;`index.html`&#41;<br>The main page of the website. There is a logo, navigation bar to *Categories*, *Shop*, *Register* and *Login* pages, a hero image, all the summary of recipes are contained and users can access to a full *Recipe* page. There is a footer with a form to subscribe to newsletters and some social icons

* **Categories** &#40;`categories_bread | cake | biscuit.html`&#41;<br>The pages where users can see recipes by category and access to a full *Recipe* page. The same header and footer are used as *Home*

* **Recipe** &#40;`recipe.html`&#41;<br>The page where the details of recipe are shown individually. The same header and footer are used as *Home*

* **Shop** &#40;`shop.html`&#41;<br>The page where users can see some baking items and purchase them on the seller's website. The same header and footer are used as *Home*

* **Register** &#40;`register.html`&#41;<br>The page where users can create an account. Once users create an account successfully, they will be led to *Profile* page. Header is different to *home* page and there is no footer

* **Login** &#40;`login.html`&#41;<br>The page where users who have an account can log in the website. Once users log in successfully, they will be led to *Profile* page. Header is different to *home* page and there is no footer

* **Profile** &#40;`profile.html`&#41;<br>The page where users will be led when they create an account or login. Users see all of their recipes with an option to edit / delete. Users can access to *Edit Recipe* page and *Delete Recipe* function by clicking a button on the recipe. There is an option to create a new recipe from this page by clicking a button and that leads to *Create Recipe* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

* **Create Recipe** &#40;`create_recipe.html`&#41;<br>The page where users can create recipes. There is no navigation link of this on the header and it can only be accessed by clicking a Create button on *Profile* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a navigation link to *Profile*

* **Edit Recipe** &#40;`edit_recipe.html`&#41;<br>The page where users can edit recipes. There is no navigation link of this on the header and it can only be accessed by clicking an Edit button on *Profile* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a navigation link to *Profile*

* **Manage Category** &#40;`manage_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can access to create, edit pages, and can delete categories. Only admin user can see a link to this page on the navigation bar. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a navigation link to *Profile*

* **Create Category** &#40;`create_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can create categories. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a navigation link to *Profile*

* **Edit Category** &#40;`edit_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can edit categories. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a navigation link to *Profile*

* **Page 404** &#40;`page_404.html`&#41;<br>The page that informs users the page does not exist and takes them back to *Home* safely. The same header and footer are used as *Home*

Summary of recipes and full recipes are accessible by any users. Summary of recipes are available on *Home* and *Categories* pages and full recipes are available on *Recipe* page.<br>


Below is the chart of the website to show the core relationships between the pages. &#40;Most of the pages are linked to each other subject to permission&#41;<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/front-end-chart.png)<br>


— Back-end —<br>
Users must have an account to post recipes so there is a *users collection* that have *username* and *password* as keys of the data. *username* in *users collections* is linked with the *username* in *recipes collection* because users who have an account can only create a recipe and they create a recipe in their own account. Same principle as *username* in *users collection* that users can only create a recipe for the categories available in a *categories collection* so it is liked with *category_name* in *recipes collection*. Categories in *categories collection* are editable by admin so it is created as an independent collection. Data in *subscription collection* is independent data for newsletters because users who do not have an account can also subscribe to it if they wish to do. The data in all the collections are retrievable and they can be identified by the key or unique id of the object. <br>


Below is the chart of the database to show the collections and their relationships.<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/back-end-chart.png)<br>

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Skeleton Plane <a name="skeleton-plane-heading"></a>
It is a mobile-first website because people usually do baking with a recipe so a good mobile-first design helps users whose main purpose is to see recipes. For users whose main purpose is to post recipes, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website. 

* [Wireframes: Home &#40;`index.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/home.png)

* [Wireframes: Categories &#40;`categories_bread | cake | biscuit.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/categories.png)

* [Wireframes: Recipe &#40;`recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/recipe.png)

* [Wireframes: Shop &#40;`shop.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/shop.png)

* [Wireframes: Register | Login &#40;`register.html` | `login.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/register-login.png)

* [Wireframes: Profile &#40;`profile.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/profile.png)

* [Wireframes: Create Recipe &#40;`create_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/create-recipe.png)

* [Wireframes: Edit Recipe &#40;`edit_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/edit-recipe.png)

* [Wireframes: Manage Category &#40;`manage_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/manage-category.png)

* [Wireframes: Create Category &#40;`create_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/create-category.png)

* [Wireframes: Edit Category &#40;`edit_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/edit-category.png)

* [Wireframes: Page 404 &#40;`page_404.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/page-404.png)

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Surface Plane <a name="surface-plane-heading"></a>
— Colour —<br>
As this website is for baking, light brownish colour is used as the main colour. Currently, the background image for the main section is decided, which is a brick style wallpaper with Tumbleweed (#eaac7f).
Other colours such as background, fonts etc are not decided yet. They will be light brown, light pink or light grey colours but the exact colours will be decided as the website is being built.

— Typography —<br>
Amatic SC is used for the main heading “Uncle Jam’s Baking Recipes” because this handwritten type of font links with recipes (hand made) very well.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/amatic-sc.png)<br>

Balsamiq Sans, which is also another type of handwritten font, is used for menu and other headings &#40;h2 - h6&#41; as it matches the image of the website well.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/balsamiq-sans.png)<br>

Nunito, which is Sans Serif type font, is used for texts on the body to give users maximum readability.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/nunito.png)<br>

<div align="right"><a href="#table-of-contents">🔝</a></div>

## WEBSITE CONSTRUCTION PLANS <a name="website-construction-plans-heading"></a>

This project contains both front-end and back-end so well-structured planning is required to do the work efficiently. Below is a summary of the plans.

1. Creating Database in MongoDB
1. Installing necessary Python frameworks, creating a Python file for the app and to test a function
1. Deploying the website in Heroku
1. Connecting Database and App
1. Creating parent HTML template with common sections (e.g. header & footer)
1. Creating *Register*, *Login*, *Profile* pages
1. Creating *Create*, *Edit* recipe pages
1. Creating *Create*, *Edit* category pages
1. Creating *Categories* recipe pages
1. Creating *Shop* page
1. Creating *404* page

Updating README.md and some testing is also done during the above process

<div align="right"><a href="#table-of-contents">🔝</a></div>

## TECHNOLOGIES USED <a name="technologies-used-heading"></a>
* [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
* [CSS3](https://en.wikipedia.org/wiki/CSS) for style
* [Python](https://www.python.org/) for backend programming language
* [Flask](https://flask.palletsprojects.com/) &#40;a micro web framework written in Python&#41; as main framework of Python
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
<!--- * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction --->
* [Google Fonts](https://fonts.google.com/) for fonts
<!--- * [Bootstrap4](https://getbootstrap.com/) (css framework) for main frame of the website --->
* [Font Awesome](https://fontawesome.com/) for icons
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging
* [Gitpod](https://www.gitpod.io/) as Integrated Development Environment &#40;IDE&#41;
* [Git](https://git-scm.com/) for local version control, keeping the files & documents
* [GitHub](https://github.com/) for online version control and keeping the files & documents
* [Heroku](https://www.heroku.com/) for and deploying the website

<div align="right"><a href="#table-of-contents">🔝</a></div>

## TESTING <a name="testing-heading"></a>
### Python <a name="python-heading"></a>
— Function —

As functions in Python are created, a manual test is carried out.

* Set up *app.py* file and test it by creating `test function` to see if "This is testing" message appears on the page

[Test Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-function.png) / 
[Test Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-function-result.png) &#40;The message is displayed so the function is working properly&#41;

— Connection with DB —

The connection between the App and MongoDB Atlas is set up so a manual test is carried out.

* `render_template` function is imported to render HTML document when the function is run. A variable called *recipes* is created to retrieve the data from *recipes collection*. Each data in *recipes collection* is retrieved by using Jinja templating language on `index.html`
 
[Connecting Function](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-db-connection.png) / 
[Connecting Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-db-connection-result.png) &#40;All the data in recipes collection is displayed so the App and database are connecting properly&#41;

— Base Template —

The base template for HTML is created so a test is carried out.

* Create `base.html` that contains all main references to external files and third-party libraries for CSS and JavaScript that are used across the entire website.  Block keyword is required to show the contents of child documents
 
[Base Template](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-base-template.png) / 
[Connecting Function Result](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/testing/python/test-base-template-result.png) &#40;All the contents of parent and child documents are displayed so the base template is working properly&#41;

<div align="right"><a href="#table-of-contents">🔝</a></div>

## PROJECT BARRIERS & SOLUTIONS <a name="barriers-solutions-heading"></a>
<!--- Retrieving data in a list --->

<div align="right"><a href="#table-of-contents">🔝</a></div>

## DEPLOYMENT <a name="deployment-heading"></a>

The website of this project requires back-end technologies such as server, application, and database so the website is deployed in [Heroku](https://www.heroku.com/) because Github can only host a static website. There are two ways to deploy a website in Heroku. One is to use Heroku Command Line Interface (CLI) and another one is to connect to GitHub repository. Connecting to GitHub repository is much easier so this website is deployed by using GitHub method.
 
Before deploying the website to Heroku, there are three important steps to follow in order to make the app work in Heroku correctly.

1. Create `requirements.txt` file that contains the names of packages being used in Python. It is important to update the file if other packages / modules are installed during the project
2. Create `Procfile` that contains the name of the application file so that Heroku knows what to run. Procfile may have a blank line so remove it as it may cause problems
3. Push them into Github

Once those steps are done, the website can be deployed and below are the steps of the deployment in Heroku.

1. Create an account in Heroku

2. Click **New** & **Create new app** to create a new app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-new-app.png)

3. Put an **App name**, which must be unique, **Choose a region** and click create app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-put-name.png)

4. Go to **Deploy** section and click **Connect to GithHub**

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-github.png)

5. Search for the repository by the repository name and connect it

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-search.png)

6. Before clicking Enable Automatic Deploys, hidden variables such as IP address, PORT, SECRET_KEY, MONGO_URI and MONGO_DATABASE need to be recorded in Heroku. Go to **Settings**, click **Reveal Config Vars** and fill out neccessary keys and values 

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-settings.png)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-vars.png)

7. Once all the hidden variables are recorded, then click **Enable Automatic Deploys** and click **Deploy Branch** &#40;Main should be selected unless you want other branches to be deployed&#41;

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-deploy.png)

8. When Heroku deploy the app correctly, there is a confirmation message and you can access the app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/deployment/dep-success.png)

<div align="right"><a href="#table-of-contents">🔝</a></div>
