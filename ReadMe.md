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
- Fetch a random recipe.
- Get recipes by cuisine type.
- Search for vegetarian recipes.

## Project Structure

### Backend (Django)

- **models.py:** Defines the `Recipe` model.
- **serializers.py:** Serializes the `Recipe` model.
- **views.py:** Contains the logic for API endpoints.
- **urls.py:** Routes API endpoints.
- **settings.py:** Configures Django settings.

### Frontend (React)

- **App.js:** Main component with routing and state management.
- **RecipeForm.js:** Component for adding a new recipe.
- **RecipeList.js:** Component for displaying a list of recipes.
- **RandomRecipe.js:** Component for fetching a random recipe.
- **VegetarianRecipes.js:** Component for fetching vegetarian recipes.

## Deployment Steps

### Frontend Deployment on AWS S3

#### Prepare Your React App for Deployment

1. **Build the React App:**
   ```bash
   npm run build
