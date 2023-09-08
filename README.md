
# HikeBikeClimb API
HikeBikeClimb is a site based on the Javascript React framework. The app uses an API created with the Django-Rest Framework to load, create, edit, and delete data. It is a site for users that likes to hike, ride bikes, and/or climb. The site gives the user tools to create and view events in these categories of sport, and to collect their specific gear in gear lists that they can update as they update their gear, to keep track of and inspire other users that are interested in different gear set ups. A user can also add posts to update the other users on the site about their journey and milestones in these sports.

## Live Site
Backend API is live here: [project-api-pj-379fd6382ab3.herokuapp.com](https://project-api-pj-379fd6382ab3.herokuapp.com/)
#### Front End Site
Frontend Is live [Here](https://project-frontend-pj-2fd2a1043672.herokuapp.com/)
## Repository
Backend repo: [github.com/PjHurtig/project-api](https://github.com/PjHurtig/project-api)
#### Front End Repository
Front end repo: [github.com/PjHurtig/project-frontend](https://github.com/PjHurtig/project-frontend)
## Table of Contents
- [HikeClimbBike API](#hikeclimbbike-api)
  * [Live Site](#live-site)
      - [Front End Site](#front-end-site)
  * [Repository](#repository)
      - [Front End Repository](#front-end-repository)
  * [Table of Contents](#table-of-contents)
  * [Testing](#testing)
    + [Manual Testing](#manual-testing)
    + [Validation Testing](#validation-testing)
  * [Deployment](#deployment)
    + [Deploying the Site to Heroku](#deploying-the-site-to-heroku)
    + [Forking the Repository on GitHub](#forking-the-repository-on-github)
    + [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
  * [Credits](#credits)
    + [Content](#content)
    + [Other programs used](#other-programs-used)
  * [Acknowledgements](#acknowledgements)


## Testing
### Manual Testing

Welcome message in root route:
![](https://i.imgur.com/FNdiqmu.png)
---
Adding /profiles to the base url shows full profile list
![](https://i.imgur.com/qRLCwp1.png)
---
Adding /profile/ and and id shows a singel profile
![](https://i.imgur.com/AuH24Js.png)
---
Adding /gearlists to the base url shows full gearlists list
![](https://i.imgur.com/eTvWd3C.png)
---
Adding /gearlists and id shows that specific gearlist 
![](https://i.imgur.com/669btx6.png)
---
Adding gearlists/?owner__profile= and an id gives all gearlists by a single user
![](https://i.imgur.com/jR1QRH1.png)
---
Adding /posts to the base url shows full posts list
![](https://i.imgur.com/yWJ95lf.png)
---
Adding /posts and id shows that specific post
![](https://i.imgur.com/exEsgad.png)
---
Adding posts/?owner__profile= and an id gives all posts by a single user
![](https://i.imgur.com/Rsc5QUp.png)
---
Adding /events to the base url shows full events list
![](https://i.imgur.com/DCxyskJ.png)
---
Adding /events and id shows that specific event
![](https://i.imgur.com/yNihzPU.png)
---
Adding events/?owner__profile= and an id gives all events by a single user
![](https://i.imgur.com/Q8sUGv1.png)
---
Addning /gearitems shows all gearitems created with info about related gearlists 
![](https://i.imgur.com/8LbgRU2.png)
---




### Validation Testing 
All .py files passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) 

## Deployment
### Deploying the Site to Heroku
1. First create a database instance on https://www.elephantsql.com/
    - Navigate to ElephantSQL.com and click “Get a managed database today”
    - Select “Try now for FREE” in the TINY TURTLE database plan
    - Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
    - In the Create New team form:
        - Add a team name (your own name is fine)
        - Read and agree to the Terms of Service
        - Select Yes for GDPR
        - Provide your email address
        - Click “Create Team”`
    - Once logged in, click 'Create New Instance'
    - Select a plan and name (this is usually the name of the project)
    - Click select region and select the region closest to you
    - Click review and create instance
    - Once created, go to the dashboard, click on the database name, and copy the URL
2. Create an account on [https://cloudinary.com/](https://cloudinary.com/) and copy the CLOUNDARY_URL from the dashboard
3. On Heroku.com, click Create New App, and create using any name
4. Go to the settings tab, click reveal config vars, and add the following key, and value pairs:
    - CLIENT_ORIGIN: this is the URL of the deployed front-end site
    - CLOUINARY_URL: the URL copied from Cloudinary
    - DATABASE_URL: the database copied from Elephant SQL
    - DISABLE_COLLECTSTATIC: set to 1
    - SECRET_KEY: any value will do
5. Open a new workspace from this repository and install any necessary packages from the requirements.txt file
6. Create an env.py file and add the lines (if committing to GitHub ensure env.py is in the .gitignore file)
    - import os 
    - os.environ['DATABASE_URL'] = 'your_database_url'
7. Enter the command 'python manage.py migrate'. This will migrate the database structure into your newly created database.
8. Go back to Heroku and click deploy. Copy the URL of the deployed site
9. Go back to the Heroku app and add a final config var of: ALLOWED_HOST with the value being the URL you just copied
10. Click open app to view the API.

### Forking the Repository on GitHub
1. On GitHub.com, navigate to the main page of the repository.
2. In the top-right corner of the page, click Fork.
3. Select an owner for the forked repository.
4. By default, forks are named the same as their upstream repositories. You can change the name of the fork to distinguish it further.
5. Optionally, add a description of your fork.
6. Choose whether to copy only the default branch or all branches to the new fork. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. By default, only the default branch is copied.
7. Click Create Fork.
### Cloning the Repository on GitHub
1. On GitHub.com, navigate to the main page of the repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.
## Credits
### Content
The website draws inspiration from the Code Institute Moments and Django Rest Framework walkthrough projects. While the foundational models were adapted from these projects, custom code was necessary to address variances in site functionality and the database schema.
## Acknowledgements 
This application was created as a portfolio 5 project for the Diploma in Full Stack Software Development from Code Institute

