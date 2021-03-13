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

## WHO'S THIS WEBSITE FOR? <a name="whos-this-website-for-heading"></a>
This is a website for people who simply love baking, or even just beginning to be interested in baking. People who would like to look at someone’s recipes for new ideas and / or who would like to share their own recipes with other people can do both on this website. The website is designed to be obvious its purpose for first-time users. Everything is laid out simply and navigated quite easily so users can adapt to the website fairly quickly, and that makes users keep coming back to the website. All the recipes are visible to any users so they do not need to create an account if they just would like to see recipes. If users would like to post their recipes, then they need to create an account but the process of creating an account is very simple. Some users may want to buy new baking items so there is a *Shop* page that uses can look at some items and purchase them on the seller's website.

<div align="right"><a href="#table-of-contents">🔝</a></div>

## WHO IS THE OWNER? <a name="who-is-the-owner-heading"></a>
I am the owner of the website. The primary goal of the website is to provide a platform that users can look at baking recipes and / or share their recipes without any hassles. There is a *Shop* page that some baking items are listed &#40;affiliate&#41; so in case users find something interesting, they can access to the seller's website for more details of the items and can also purchase them. I can get a commission from the seller for any items being sold through my website and this is also one of the goals. I would like to collect their e-mail address for newsletters to expand the community.

<div align="right"><a href="#table-of-contents">🔝</a></div>

## UX 5 PLANES <a name="ux5-planes-heading"></a>

### Strategy Plane <a name="strategy-plane-heading"></a>

The website is designed for those who love baking, and who are interested in baking. People who have been baking might want to share their knowledge with other people as it gives them great feeling and motivation, so by following very simple registration steps, they can create an account and post their recipes in a well-structured format. People who have less experience in baking and would just like to see recipes, they can do it simply by visiting the website, where all the recipes are shown by posted date, or they can see them by category &#40;bread, cake, biscuit&#41; on different pages. There is a search field on the website so they can search for specific recipes by keywords. To see recipes, users do not need to register so it is hassle-free. There is a *shop* page that has a number of baking items in an affiliate style so in case users would like to purchase something, they can do it by clicking the link and it leads users to the website of the sellers. The design of the website is meaningful and simple so that the purpose of the website is very clear for first-time users, and they can easily adapt to the website. Owner’s main goal is to provide a community platform that is easy to use whether they are first-time or returning users, and this is the key to grow the community. To achieve this, all the contents and functions are laid out as the user’s first concept.

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
| Subscribe Newsletter                        |     4      |            4            |
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
*    Simple design Home page that first-time users can recognise the purpose of the website easily. All the recipes are shown on the home page &#40;R&#41;
*    Categories &#40;Bread, Cake and Biscuit&#41; pages that users can see recipes by the categories &#40;R&#41;
*    Shop page that users can see some baking items, which are linked to the seller’s website
*    Register page that users can create an account to post and edit recipes
*    Login page that users can log in to the website
*    Logout function that users can log out
*    Profile page that users can see all the recipes and access to create, edit and delete recipes 
*    Create Recipe page that users can create their recipes and post them &#40;C&#41;
*    Edit Recipe page that users can edit their recipes &#40;U&#41;
*    Delete Recipe function that users can delete their recipes &#40;D&#41;
*    Manage Category functions that only <ins>admin user</ins> &#40;owner&#41; can create, edit and delete categories &#40;C & U & D&#41;
*    Search by keywords function that users can search for specific recipes
*    Subscribe Newsletter section to collect users email addresses
*    404 page that takes users back to the home page of the website safely  

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Structure Plane <a name="structure-plane-heading"></a>

— Front-end —<br>
The website consists of a **Home** page with **14 other core pages**.
*    **Home** &#40;`index.html`&#41;<br>The main page of the website. There is a logo, navigation bar to *Categories*, *Shop*, *Register* and *Login* pages, a hero image, all the summary of recipes are contained and users can access to a full *Recipe* page. There is a footer with a form to subscribe to newsletters and some social icons

*    **Categories** &#40;`categories_bred | cake | biscuit.html`&#41;<br>The pages where users can see recipes by category and access to a full *Recipe* page. The same header and footer are used as *Home*

*    **Recipe** &#40;`recipe.html`&#41;<br>The page where the details of recipe are shown individually. The same header and footer are used as *Home*

*    **Shop** &#40;`shop.html`&#41;<br>The page where users can see some baking items and purchase them on the seller's website. The same header and footer are used as *Home*

*    **Register** &#40;`register.html`&#41;<br>The page where users can create an account. Once users create an account successfully, they will be led to *Profile* page. Header is different to *home* page and there is no footer

*    **Login** &#40;`login.html`&#41;<br>The page where users who have an account can log in the website. Once users log in successfully, they will be led to *Profile* page. Header is different to *home* page and there is no footer

*    **Profile** &#40;`profile.html`&#41;<br>The page where users are led when they create an account or login. Users see all of their recipes with an option to edit / delete. Users can access to *Edit Recipe* page and *Delete Recipe* function by clicking a button on the recipe. There is an option to create a new recipe from this page by clicking a button and that leads to *Create Recipe* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Create Recipe** &#40;`create_recipe.html`&#41;<br>The page where users can create recipes. There is no navigation link of this on the header and it can only be accessed by clicking a Create button on *Profile* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Edit Recipe** &#40;`edit_recipe.html`&#41;<br>The page where users can edit recipes. There is no navigation link of this on the header and it can only be accessed by clicking an Edit button on *Profile* page. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Manage Category** &#40;`manage_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can access to create, edit pages, and can delete categories. Only admin user can see a link to this page on the navigation bar. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Create Category** &#40;`create_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can create categories. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Edit Category** &#40;`edit_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can edit categories. The same header and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*

*    **Page 404** &#40;`page_404.html`&#41;<br>The page that informs users the page does not exist and takes them back to *Home* safely. The same header and footer are used as *Home*

Summary of recipes and full recipes are accessible by any users. Summary of recipes are available on *Home* and *Categories* pages and full recipes are available on *Recipe* page.<br>


Below is the chart of the website to show the core relationships between the pages. &#40;Most of the pages are linked to each other subject to permission&#41;<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/front-end-chart.png)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/front-end-chart-50.png)<br>

— Back-end —<br>
Users must have an account to post recipes so there is a *users collection* that have *username* and *password* as keys of the data. *username* in *users collections* is linked with the *username* in *recipes collection* because users who have an account can only create a recipe and they create a recipe in their own account. Same principle as *username* in *users collection* that users can only create a recipe for the categories available in a *categories collection* so it is liked with *category_name* in *recipes collection*. Categories in *categories collection* are editable by admin so it is created as an independent collection. Data in *subscription collection* is independent data for newsletters because users who do not have an account can also subscribe to it if they wish to do. The data in all the collections are retrievable and they can be identified by the key or unique id of the object. <br>


Below is the chart of the database to show the collections and their relationships.<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/back-end-chart.png)<br>


![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/back-end-chart-50.png)<br>

<div align="right"><a href="#table-of-contents">🔝</a></div>

### Skeleton Plane <a name="skeleton-plane-heading"></a>
It is a mobile-first website because people usually do baking with a recipe so a good mobile-first design helps users whose purpose is to see recipes. There are wireframes of mobile and desktop sizes for all the core pages of the website. 

*    [Wireframes: Home &#40;`index.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/home.png)

*    [Wireframes: Categories &#40;`categories_bred | cake | biscuit.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/categories.png)

*    [Wireframes: Recipe &#40;`recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/recipe.png)

*    [Wireframes: Shop &#40;`shop.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/shop.png)

*    [Wireframes: Register | Login &#40;`register.html` | `login.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/register-login.png)

*    [Wireframes: Profile &#40;`profile.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/profile.png)

*    [Wireframes: Create Recipe &#40;`create_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/create_recipe.png)

*    [Wireframes: Edit Recipe &#40;`edit_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/edit_recipe.png)

*    [Wireframes: Manage Category &#40;`manage_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/manage_category.png)

*    [Wireframes: Create Category &#40;`create_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/create_category.png)

*    [Wireframes: Edit Category &#40;`edit_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/edit_category.png)

*    [Wireframes: Page 404 &#40;`page_404.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/assets/readme/ux/page_404.png)

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
