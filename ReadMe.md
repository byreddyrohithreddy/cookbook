# Project Documentation: Recipe App

## Overview

This project consists of a Recipe App built using React for the frontend and Django for the backend. The app allows users to add new recipes, fetch a random recipe, get recipes by cuisine type, and search for vegetarian recipes. The frontend is deployed on AWS S3, while the backend runs on an AWS EC2 instance.

## Tech Stack

- **Frontend:** React.js
- **Backend:** Django REST framework
- **Deployment:**
  - Frontend: AWS S3
  - Backend: AWS EC2

## Features

- Add a new recipe.
- ![image](https://github.com/user-attachments/assets/224a4b8b-5500-438f-9ece-84db47e330d7)

- Get recipes by cuisine type.
- ![image](https://github.com/user-attachments/assets/e1db997c-8ab3-43da-9163-e3e33f7d8c0f)

- Fetch the vegetarian recipes.
- ![image](https://github.com/user-attachments/assets/cc48763c-74ef-41b3-a25b-7a417f40870f)
- 
- Get Most used ingredients
- ![image](https://github.com/user-attachments/assets/5f67d300-742a-43e2-94a9-ad5117724977)

## Project Structure

### Backend (Django)

- **models.py:** Defines the `Recipe` model.
- **serializers.py:** Serializes the `Recipe` model.
- **views.py:** Contains the logic for API endpoints.
- **urls.py:** Routes API endpoints.
- **settings.py:** Configures Django settings.
  
![image](https://github.com/user-attachments/assets/b2476f84-0d6d-4c6a-bd52-4bfe41f28db9)

### Frontend (React)

- **App.js:** The main component is routing and state management.
- **RecipeForm.js:** Component for adding a new recipe.
- **RecipeList.js:** Component for displaying a list of recipes.
- **RandomRecipe.js:** Component for fetching a random recipe.
- **VegetarianRecipes.js:** Component for fetching vegetarian recipes.
  
![image](https://github.com/user-attachments/assets/bd7c2060-e89b-4ffb-b513-5a9a9a6adf0e)

## Deployment Steps

# Backend Deployment on AWS EC2

## Launch an EC2 Instance  and upload the Django code:

1. Select an Ubuntu AMI.
2. Configure instance details, add storage and configure security groups (open port 80 for HTTP and port 8000 for Django).
3. After creating an instance, upload the recipe-project file to the ec2 using scp or rsync
4. Install the dependencies required
5. Start the server using nohup by running the command below
   ``` nohup python3 manage.py runserver 0.0.0.0:8000 & ```
6. This will run the server on the ec2 instance

### Frontend Deployment on AWS S3

1. After creating the backend server get the public ip of the ec2 instance, this will the ip for endpoints in react app.
2. Prepare the react app by changing the endpoints to the ip
3. which need to build the app using
   ``` npm run build ```
4. Create a s3 bucket and make bucket properties set to index.html
5. Upload the build files to s3 bucket
6. we will get the file URL from the s3 bucket properties

### Challenges:
- I couldn't use Cloudfront and VPC for EC2 because they are paid types and can't be used for the free tier version.

### Final URL
I have finished all the steps, and the final deployed URL is
URL:  http://s3recipe.s3-website.us-east-2.amazonaws.com/

### References:
1. https://docs.aws.amazon.com/s3/?icmpid=docs_homepage_featuredsvcs
2. https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_featuredsvcs
3. https://legacy.reactjs.org/docs/getting-started.html
4. https://docs.djangoproject.com/en/5.0/
