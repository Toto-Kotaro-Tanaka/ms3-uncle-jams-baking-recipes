![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/other/readme-logo.png)

# Uncle Jam's Baking Recipes <a name="top"></a>

This is a website for baking recipes of bread, cakes, and biscuits. I create this for **Milestone Project 3 (Python and Data-Centric Development), Full Stack Software Development** in [Code Institute](https://codeinstitute.net/), Ireland.
It is a mobile-first & responsive website and the link to the website is available [HERE.](https://ms3-uncle-jams-baking-recipes.herokuapp.com/home)

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/other/mockup.png)

## WHO'S THIS WEBSITE FOR?

This is a website for people who simply love baking, or even just beginning to be interested in baking. People, who would like to see someone’s recipes for new ideas and&#47;or to share their own recipes with other people, can do both on this website. The website is designed to be obvious its purpose for first-time users. Everything is laid out simply and navigated quite easily so users can adapt to the website fairly quickly, and that makes users keep coming back to the website. All the recipes are visible to any users so they do not need to create an account if they just would like to see recipes. If users would like to create and post their recipes, then they need to create an account but the process of creating an account is very simple. Some users may want to buy new baking items so there is a _Shop_ page where uses can look at some items and purchase them on the seller's website. There is a function to subscribe to newsletter to get engaged in what’s happening in baking and the community.

<div align="right"><a href="#top">🔝</a></div>

## WHO IS THE OWNER?

I am the owner of the website. The primary goal of the website is to provide a platform that users can see baking recipes and&#47;or share their recipes without any hassles. There is a _Shop_ page that some baking items are listed &#40;affiliate&#41; so in case users find something interesting, they can access the seller's website for more details of the items and can also purchase them. I can get a commission from the seller for any items being sold through my website and this is also one of the goals. I would like to collect their e-mail address for newsletters to expand the community for further business opportunities.

<div align="right"><a href="#top">🔝</a></div>

## UX 5 PLANES

### Strategy Plane

The website is designed for those who love baking, and who are interested in baking. People who have been baking might want to share their knowledge with other people as it gives them great feeling and motivation, so by following very simple registration steps, they can create an account and post their recipes in a well-structured format. People who have less experience in baking and would just like to see recipes, they can do it simply by visiting the website where all the recipes are shown by posted date, or they can see them by category &#40;bread, cake, biscuit&#41; on different pages. There is a search function on the website so they can search for specific recipes by a keyword&#40;s&#41;. To see recipes, users do not need to register so it is hassle-free. There is a _shop_ page that has some baking items in an affiliate style so in case users would like to purchase something, they can do it by clicking the link and it leads users to the website of the sellers. The design of the website is meaningful and simple so that the purpose of the website is very clear for first-time users, and they can easily adapt to the website. This also applies to all the functions to create, post, edit and delete recipes for regular users. The owner’s main goal is to provide a baking recipe platform that is easy to use whether they are first-time or returning users, and this is the key to grow the community for further business opportunities. To achieve this, the website is designed and created by user first concept.

All the functions on the tables below are minimum requirements on the website to achieve the current user's and owner's goals. &#40;On a scale of 1 &#91;least&#93; - 5 &#91;most&#93;&#41;

| Opportunity                                 | Importance | Viability / Feasibility |
| :------------------------------------------ | :--------: | :---------------------: |
| Register                                    |     5      |            5            |
| Login / Log out                             |     5      |            5            |
| Create / Edit / Delete Recipes              |     5      |            4            |
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

> **Note:**<br>
> During the project, decide to add pagination as it makes the website much neater so it is implemented in the current project

### Scope Plane

To achieve user and owner’s goals, below are the minimum features to be included in this project. Also, **CRUD** &#40;Create, Read, Update, and Delete&#41; functions are required for this project so these are implemented as a part of essential features.

- Simple design Home page that first-time users can recognise the purpose of the website easily. All the recipes are shown on _Home_ page &#40;R&#41;
- Categories &#40;Bread, Cake and Biscuit&#41; pages where users can see recipes by the categories &#40;R&#41;
- Shop page where users can see some baking items linked to the seller’s website
- Register page where users can create an account to create, post and edit recipes
- Login page where users can log in to the website
- Logout function that users can log out the website
- Profile page where users can see all their recipes and access to create, post, edit and delete recipes
- Create Recipe page where users can create and post their recipes&#40;C&#41;
- Edit Recipe page where users can edit their recipes &#40;U&#41;
- Delete Recipe function that users can delete their recipes &#40;D&#41;
- Manage Category page and functions that only <ins>admin user</ins> &#40;owner&#41; can create, edit and delete categories &#40;C & U & D&#41;
- Search by a keyword&#40;s&#41; function that users can search for specific recipes
- Subscribe to newsletter function to collect users email addresses
- 404 page that appears for invalid url and takes users back to _Home_ page of the website safely

> **Note:**<br>
> Initially, only 3 fixed categories are planned for recipes, however as the project is created, discover that newly created category can be implemented on the website by using loop so categories are note limited. &#40;e.g. If the admin decides to create a new category called "Birthday", it can be implemented to the website automatically&#41;

### Structure Plane

— **Front-end** —

The website consists of **Home** page with **13 other core pages**.

- **Home** &#40;`index.html`&#41;<br>The main page of the website. There is a logo, navigation bar to _Categories_, _Shop_, _Register_ & _Login_ pages, a title, a hero image. All the summary of recipes are contained and users can access a full _Recipe_ page. There is a footer with a form to subscribe to newsletter and some social icons

- **Search Result** &#40;`search.html`&#41;<br>The pages where users can see recipes by search and access a full _Recipe_ page. The same navigation bar and footer are used as _Home_ \*Idea of having this page comes up during the project

- **Categories** &#40;`categories_<category_name>.html`&#41;<br>The pages where users can see recipes by category and access a full _Recipe_ page. The same navigation bar and footer are used as _Home_

- **Recipe** &#40;`recipe.html`&#41;<br>The page where a full recipe is shown individually. The same navigation bar and footer are used as _Home_

- **Shop** &#40;`shop.html`&#41;<br>The page where users can see some baking items and purchase them on the seller's website. The same navigation bar and footer are used as _Home_

- **Register** &#40;`register.html`&#41;<br>The page where users can create an account. Once users create an account successfully, they will be led to _Profile_ page. The navigation bar is different to _Home_ page, in which users can go back to _Home_ page by clicking Uncle Jam's icon, and there is no footer

- **Login** &#40;`login.html`&#41;<br>The page where users who have an account can log in to the website. Once users log in successfully, they will be led to _Profile_ page. The navigation bar is different to _Home_ page, in which users can go back to _Home_ page by clicking Uncle Jam's icon, and there is no footer

- **Profile** &#40;`profile.html`&#41;<br>The page where users will be led when they create an account or login. Users see all of their recipes with an option to edit&#47;delete. Users can access to _Edit Recipe_ page and _Delete Recipe_ function by clicking a button on the recipe. There is an option to create a new recipe from this page by clicking a button and that leads to _Create Recipe_ page. The same navigation bar and footer are used as _Home_ but there is a _Logout_ function instead of _Register_ and _Login_. There is also a link to _Profile_ page on the navigation bar

- **Create Recipe** &#40;`create_recipe.html`&#41;<br>The page where users can create and post recipes. There is no link on the navigation bar and it can only be accessed by clicking a Create Recipe button on _Profile_ page. The page style is same as _Register | Login_, and users can go back to _Profile_ page by clicking gingerbread man icon or cancel button

- **Edit Recipe** &#40;`edit_recipe.html`&#41;<br>The page where users can edit recipes. There is no link on the navigation bar and it can only be accessed by clicking an Edit button on _Profile_ page. The page style is same as _Register | Login_, and users can go back to _Profile_ page by clicking gingerbread man icon or cancel button

- **Manage Category** &#40;`manage_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can access to create and edit category pages as well as to delete categories. Only admin user can have an access to this page by a navigation link that appears for admin _Profile_ page. The page style is same as _Home_

- **Create Category** &#40;`create_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can create categories. The page style is same as _Register | Login_, and admin user can go back to _Manage Category_ page by clicking tools icon or cancel button

- **Edit Category** &#40;`edit_category.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can edit categories. The page style is same as _Register | Login_, and admin user can go back to _Manage Category_ page by clicking tools icon or cancel button

- **Page 404** &#40;`page_404.html`&#41;<br>The page that informs users the page not found and takes them back to _Home_ page safely. The page style is same as _Register | Login_.

Summary of recipes and full recipes are accessible by any users. Summary of recipes are available on _Home_ and _Categories_ pages and full recipes are available on _Recipe_ page.

Below is the chart of the website to show the core relationships between the pages. &#40;Most of the pages are linked to each other subject to permission&#41;<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/front-end-chart.png)<br>

— **Back-end** —<br>
Users must have an account to create recipes so there is a **users collection** that has _<ins>username</ins>_ and _<ins>password</ins>_ as keys of the data. _<ins>username</ins>_ in **users collections** is linked with the _<ins>username</ins>_ in **recipes collection** because users who have an account can only create a recipe and they create a recipe in their own account. Same principle as _<ins>username</ins>_ in **users collection** that users can only create a recipe for the categories available in a **categories collection** so it is liked with _<ins>category_name_</ins> in **recipes collection**. Categories in **categories collection** are editable by admin so it is created as an independent collection. Data in **subscription collection** is independent data for newsletters because users who do not have an account can also subscribe to it if they wish to do. The data in all the collections are retrievable and can be identified by the key or unique id of the object.

Below is the chart of the database to show the collections and their relationships.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/back-end-chart.png)<br>

### Skeleton Plane

It is a mobile-first website because people usually bake with a recipe so a good mobile-first design helps users whose main purpose is to see recipes. For users whose main purpose is to create and post recipes, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

- [Wireframes: Home &#40;`index.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/home.png)

- [Wireframes: Categories &#40;`categories_bread | cake | biscuit.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/categories.png)

- [Wireframes: Recipe &#40;`recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/recipe.png)

- [Wireframes: Shop &#40;`shop.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/shop.png)

- [Wireframes: Register | Login &#40;`register.html` | `login.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/register-login.png)

- [Wireframes: Profile &#40;`profile.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/profile.png)

- [Wireframes: Create Recipe &#40;`create_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/create-recipe.png)

- [Wireframes: Edit Recipe &#40;`edit_recipe.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/edit-recipe.png)

- [Wireframes: Manage Category &#40;`manage_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/manage-category.png)

- [Wireframes: Create Category &#40;`create_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/create-category.png)

- [Wireframes: Edit Category &#40;`edit_category.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/edit-category.png)

- [Wireframes: Page 404 &#40;`page_404.html`&#41;](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/page-404.png)

> **Note:**<br>
> Small design amendments during the project. Some pages have a heading section only

### Surface Plane

— **Colour** —

As this is a baking recipes website, **Cafe Noir** &#40;#493323&#41; is used as the main colour of the website. It is used as it is on some headings, texts as well as the navigation bar, footer, and slightly transparentised colour is used for some background. **Linen** &#40;#FBEADE&#41; and **Apricot** &#40;#FFD5B7&#41; are used for some text and background when it needs contrast. **Mango Tango** &#40;#FF7C3E&#41; and **Flame** &#40;#E84610&#41; are used when it needs an accent on the website such as See Recipe button, flash messages and hover effect.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/colours.png)

— **Typography** —

**Amatic SC** is used for the main heading “Uncle Jam’s Baking Recipes” &#40;h1&#41; and headings of other pages &#40;h2&#41; because this handwritten type of font links with recipes (hand made) very well.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/amatic-sc.png)

**Balsamiq Sans**, which is also another type of handwritten font, is used for menu and other headings &#40;h3 - h6&#41; as it matches the image of the website well.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/balsamiq-sans.png)

**Nunito**, which is Sans Serif type font, is used for texts on the body to give users maximum readability.

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/ux/nunito.png)

<div align="right"><a href="#top">🔝</a></div>

## WEBSITE CONSTRUCTION PLANS

This project contains both front-end and back-end so well-structured planning is required to do the work efficiently. Below is a summary of the plans.

1. Creating Database in MongoDB
1. Installing necessary Python frameworks, creating a Python file for the app and testing a function
1. Deploying the website in Heroku
1. Connecting Database and App
1. Creating parent HTML template with common sections &#40;e.g. header & footer&#41;
1. Creating _Register_, _Login_, _Profile_ pages
1. Creating _Create_, _Edit_ recipe pages
1. Creating _Create_, _Edit_ category pages
1. Creating _Categories_ recipe pages
1. Creating an individual _Recipe_ page
1. Creating _Shop_ page
1. Creating _404_ page

Updating README.md and some testing is also done during the above process

<div align="right"><a href="#top">🔝</a></div>

## FEATURES

### Existing Features

- Create with **HTML5**, **CSS3** &#40;with Material Design for Bootstrap&#41;, **JavaScript**, **Python** &#40;Flask&#41;, **MongoDB** &#40;Atlas&#41;
- It consists of 1 base html file and 14 other html files
- Modal for "Create Recipe" instructions and confirmation for "Delete" function
- [BBC Good Food](https://www.bbcgoodfood.com/) for recipes
- All the [features planned on scope plane](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/other/scope-plane.png) and Pagination

### Features Left To Implement

- **Resetting Password When Users Forget It:** To achieve this, an email address is probably required for creating an account. Current primary purpose of the website is to provide easy access to the platform as well as I do not know how to implement this with my current skills, decide to leave this out
- **Upload Image For Each Recipe:** Image data cannot be stored in MongoDB so this is not possible with the current project however having image for recipes is achieved by using image URL
- **Review By Other Users:** I do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out
- **“Like” Reaction By Other Users:** I do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out
- **Customise Pagination Page Display:** Manage to do pagination as it is essential to have to make the website neat, however I do not know how to customise pagination page display &#40;e.g. When there are more recipes, it will show page 1, 2, 3, 4, 5, 6, 7...&#41; and I do not have time to look into details so decide to leave it as it is

<div align="right"><a href="#top">🔝</a></div>

## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Material Design for Bootstrap 5 & 4](https://mdbootstrap.com/) &#40;an open-source toolkit based on Bootstrap for developing Material Design&#41; for mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Flask](https://flask.palletsprojects.com/) &#40;a micro web framework written in Python&#41; as main framework of Python
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment &#40;IDE&#41;
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website

<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

### Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Adobe](https://www.adobe.com/ie/photoshop/online/resize-image.html) for resizing images
- [PNG to ICO](https://hnet.com/png-to-ico/) for converting png to ico for favicon
- [removebg](https://www.remove.bg/) for removing background images
- [Transparent Textures](https://www.transparenttextures.com/) for creating background image
- [Canva](https://www.canva.com/) for creating logos and some images
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php) for mockup
- [Autoprefixer](https://autoprefixer.github.io/) for parsing CSS and add vendor prefixes
- [W3C Markup Validation Service](https://validator.w3.org/) for testing html code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing css code
- [jshint](https://jshint.com/) for testing javascript code
- [PEP8 Online](http://pep8online.com/) for checking python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

<div align="right"><a href="#top">🔝</a></div>

## TESTING

Testing report is available **[TESTING.md](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/TESTING.md)**

<div align="right"><a href="#top">🔝</a></div>

## PROJECT BARRIERS & SOLUTIONS

— **Typos** —

There are a few issues caused by typos and mislocating bracket. Nothing technical and these are just careless mistakes but spend some time trying to figure out what wrong it is. The solution for this is to be more careful of what you type, especially, something that the editor does not show as an error and need to be patient to go through each code again.

— **Text Wrap** —

For some reason, some texts in heading are not wrapped and just keep going to the right. Look up the solution on internet and found that `word-wrap: break-word;` css code can be used to prevent this

— **Retrieving Data in List** —

On `edit_recipe` function, data needs to be retrieved from the database. Not sure how to do it for the data in a list so look up the solution on internet and find a [Stackoverflow post](https://stackoverflow.com/questions/17575276/how-can-i-print-a-mongodb-list-in-a-jinja2-template) that gives me the solution for this

— **Targeting Specific Delete Item in Modal** —

Set up a modal for delete function to prevent users from deleting items unintentionally, however when modal is open, it targets the first item and not the specified item. Not sure what the issue is but keep testing it and come up with an idea of putting object id as a part of id &#40;`id="modal-delete{{ recipe._id }}"`&#41; and somehow make it work

— **Form Validation** —

There are some headings for dropdown menu for creating recipes. Even though those headings are disabled, users actually can submit it, if they do not open the options in dropdown menu, and it stores an empty value in the database. It causes issues for `category_name` as there must be a value for this. Try a few ways to solve the issue and come up with an idea to allocate "other" as a category. Currently form is validated by html only but by using Flask form validation WTForms, this might be achieved better, however, this is a new module for me and currently do not have time to learn it so decide to keep the form as it is.

— **Pagination** —

Initially don't plan to implement this on the project but as a number of recipes increases, decide to do it to make the website look better. Watch [Corey Schafer's youtube tutorial](https://www.youtube.com/watch?v=PSWf2TjTGNY), follow [Pagination Demo](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) but cannot make pagination work. Find a recent post on slack about pagination so follow the threads and then look at [Ed Bradley's](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/other/pagination-ed.png) code on his project and use it to make it work. It works as pagination but still do not understand the logic of this very well

— **Defensive Programme** —

<div align="right"><a href="#top">🔝</a></div>

## VERSION CONTROL

[Git](https://git-scm.com/) as a local repository and [GitHub](https://github.com/) as a remote repository are used for the project, and below is how I use these as the version control for the project.

— **Setting Up** —

1. Create a **remote repository** in GitHub by clicking **"New repository"** on the main page<br>
   ![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/version-control/version-control-1.png)<br>

2. Use **Code Institute Template**, put the repository name and click Create Repository making sure to select public<br>
   ![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/version-control/version-control-2.png)<br>

3. Open the repository with [Gitpod](https://www.gitpod.io/) which is my Integrated Development Environment (IDE). By using Code Institue Template, initialisation including initial commit is done so no need to do `git init` command when open IDE, or to use `git push -u origin main` command for my first commit. `gitignore` file, which is very important for the project including some confidential information, is created with Code Institute template so not necessary to create it<br>
   ![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/version-control/version-control-3-1.png)<br>
   ![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/version-control/version-control-3-2.png)<br>

— **Commitments** —

- When a section or even a group of work are completed, they are committed in git and pushed into GitHub, in order to make sure to keep the history of the work logged properly and not to lose the work in unexpected situations. Below commands are used for this.

```
* git status | To check the status of new/modified folders, files, and documents
* git add . | To put all new and updated work on the stage in git
  git add <specific file> is used when different types of work are done but do not want to commit everything on the same commitment
* git commit -m "Example commit" | To commit the work on the stage in git before pushing it to GitHub
* git push | To update the repository in GitHub for main branch
  git push origin <branch name> is used when pushing git into GitHub for sub branches
```

> **Note:**<br>
> During the project, I learn a better way of keeping commit messages so follow this [article](https://chris.beams.io/posts/git-commit/)

— **Branches** —

- When some testing is needed, create a branch and test is on it instead of using main branch. When the testing is successful, then merge the branch into main, when it is not, leave the branch unmerged and keep working on main branch. Below commands are used for this.

```
* git branch <branch name> | To create a new branch
* git checkout <branch name> | To switch branch
* git branch | To check current branch
* git merge <branch name> | To merge sub branch into main, do this on main branch
```

> **Note:**<br>
> I understand that same sub branch can be used as many times as I want to, however I create a new branch for each test because my knowledge of git is not the best and sometimes I am not 100% sure if I do it right. I would like to improve more on the usage of git and version control for my next project

> There is one [commit message](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/version-control/commit-msg.png) does not correspond to what happen. I commit it from sub branch presuming there are only minor changes, however, it seems it does it from main branch somehow

<div align="right"><a href="#top">🔝</a></div>

## DEPLOYMENT

The website of this project requires back-end technologies such as server, application, and database so the website is deployed in [Heroku](https://www.heroku.com/), which is a cloud platform with a service supporting several programming languages, as GitHub can only host a static website. There are two ways to deploy a website in Heroku. One is to use Heroku Command Line Interface (CLI) and another one is to connect to GitHub repository. Connecting to GitHub repository is much easier and recommended by a tutor so this website is deployed by using GitHub method.

Before deploying the website to Heroku, there are three important steps to follow in order to make the app work in Heroku correctly.

1. Create `requirements.txt` file that contains the names of packages being used in Python. It is important to update the file if other packages or modules are installed during the project
2. Create `Procfile` that contains the name of the application file so that Heroku knows what to run. Procfile may have a blank line when it is created so remove it as it may cause problems
3. Push them into Github

Once those steps are done, the website can be deployed and below are the steps of the deployment in Heroku.

1. Create an account in Heroku

2. Click **New** & **Create new app** to create a new app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-new-app.png)

3. Put an **App name**, which must be unique, **Choose a region** and click create app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-put-name.png)

4. Go to **Deploy** section and click **Connect to GithHub**

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-github.png)

5. Search for the repository by the repository name and connect it

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-search.png)

6. Before clicking Enable Automatic Deploys, hidden variables such as IP address, PORT, SECRET_KEY, MONGO_URI and MONGO_DATABASE need to be recorded in Heroku. Go to **Settings**, click **Reveal Config Vars** and fill out necessary keys and values

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-settings.png)<br>

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-vars.png)

7. Once all the hidden variables are recorded, then click **Enable Automatic Deploys** and click **Deploy Branch** &#40;Main should be selected unless you want other branches to be deployed&#41;

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-deploy.png)

8. When the app is deployed by Heroku correctly, there is a confirmation message and you can access the app

![image](https://github.com/Toto-Kotaro-Tanaka/ms3-uncle-jams-baking-recipes/blob/master/readme/deployment/dep-success.png)

<div align="right"><a href="#top">🔝</a></div>

## CREDITS

### Code

— **HTML5** —

- [MDB Navbar](https://mdbootstrap.com/docs/standard/navigation/navbar/) for navigation bar
- [MDB Forms & Input](https://mdbootstrap.com/docs/standard/forms/overview/) for input forms
- [MDB Cards](https://mdbootstrap.com/docs/standard/components/cards/) for recipe summary display
- [MDB Modal](https://mdbootstrap.com/docs/standard/components/modal/) for delete confirmation & recipe instructions
- [Bootstrap Dropdowns](https://getbootstrap.com/docs/5.0/components/dropdowns/) for dropdown menus

— **CSS3** —

- [Html Code Generator](https://www.html-code-generator.com/css/speech-bubble-generator) for speech bubble
- [Codepen CSS Bouncing Arrow](https://codepen.io/bitstarr/pen/XjaJGz) for bouncing arrow

— **JavaScript** —

- [Sanwebe](https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery) for adding input fields

— **Python** —

- [Ed Bradley](https://github.com/Edb83/self-isolution/blob/master/app.py) for pagination

> **Note:**
> All credits are also mentioned on the files

### Contents

— **Recipes** —

All recipes are from [BBC Good Food](https://www.bbcgoodfood.com/)

- [Triple chocolate & peanut butter layer cake](https://www.bbcgoodfood.com/recipes/triple-chocolate-peanut-butter-layer-cake)
- [Rustic bread](https://www.bbcgoodfood.com/recipes/rustic-bread)
- [Hedgehog rolls](https://www.bbcgoodfood.com/recipes/hedgehog-rolls)
- [Lemon biscuits](https://www.bbcgoodfood.com/recipes/lemon-kisses)
- [Seed & grain cottage loaf](https://www.bbcgoodfood.com/recipes/seed-grain-cottage-loaf)
- [Ginger biscuits](https://www.bbcgoodfood.com/recipes/ginger-biscuits)
- [Easy vanilla cake](https://www.bbcgoodfood.com/recipes/easy-vanilla-cake)
- [Florentine biscuits](https://www.bbcgoodfood.com/recipes/florentine-biscuits)
- [Easy millionaire’s shortbread](https://www.bbcgoodfood.com/recipes/easy-millionaires-shortbread)
- [Mary Berry’s orange layer cake
  ](https://www.bbcgoodfood.com/recipes/mary-berrys-orange-layer-cake)
- [Chocolate fudge crinkle biscuits](https://www.bbcgoodfood.com/recipes/chocolate-fudge-crinkle-biscuits)
- [Luscious lemon baked cheesecake](https://www.bbcgoodfood.com/recipes/luscious-lemon-baked-cheesecake)
- [Honey & almond layer cake](https://www.bbcgoodfood.com/recipes/honey-almond-layer-cake)
- [Manchego & chorizo melting biscuits](https://www.bbcgoodfood.com/recipes/manchego-chorizo-melting-biscuits)
- [Soft burger buns](https://www.bbcgoodfood.com/recipes/soft-burger-buns)
- [Easy sourdough bread](https://www.bbcgoodfood.com/recipes/cheats-sourdough)
- [Basic granary bread dough (for rolls or a large loaf)](https://www.bbcgoodfood.com/recipes/basic-granary-bread-dough-rolls-or-large-loaf)
- [Ham & tomato Stromboli](https://www.bbcgoodfood.com/recipes/ham-tomato-stromboli)
- [Turkish-style sharing bread](https://www.bbcgoodfood.com/recipes/turkish-style-sharing-bread)
- [Dundee cake](https://www.bbcgoodfood.com/recipes/dundee-cake)
- [Vanilla cupcake bouquet](https://www.bbcgoodfood.com/recipes/vanilla-cupcake-bouquet)
- [Pistachio & milk chocolate squares](https://www.bbcgoodfood.com/recipes/pistachio-milk-chocolate-squares)

— **Affiliate** —

All affiliates are from [Amazon Affiliate Programe](https://affiliate-program.amazon.com/)

- [Cake Decorating Equipment](https://www.amazon.co.uk/gp/product/B07N1JB9V7/)
- [Set of 8 Non Stick Baking Tray](https://www.amazon.co.uk/gp/product/B07B3XVN2V/)
- [Stainless Steel Angled Icing Spatulas](https://www.amazon.co.uk/gp/product/B089F8XXLM/)
- [Kenwood Mary Berry Special Edition Chef Elite Stand Mixer](https://www.amazon.co.uk/gp/product/B07XVF56FM/)
- [Mary Berry's Baking Bible](https://www.amazon.co.uk/gp/product/1846077850/)
- [Russell Hobbs 23620 Compact Fast Breadmaker](https://www.amazon.co.uk/gp/product/B01HMITHY2/)

### Media

— **Logo & Favicon & Other Images** —

- Logo and favicon created by me using [canva](https://www.canva.com/)
- Other images are from elements in [canva](https://www.canva.com/)

<div align="right"><a href="#top">🔝</a></div>

## ACKNOWLEDGEMENTS

I would like to thank ;

- My mentor, **Spencer Barriball**, who goes through the project with me and gives me some advice to improve UI and UX
- **Ed Bradley** who gives me advice on several queries and difficulties I have throughout the project
- Code Institute Tutor **Alan** who gives me guidance on how to solve the issue
- **Code Institute Slack Members** who give me advice on queries I have throughout the project

<div align="right"><a href="#top">🔝</a></div>
