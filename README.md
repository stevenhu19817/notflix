# Notflix

## Overview

Notflix is a project that simulates a simplified version of the Netflix interface. The backend system provides API support for retrieving, storing, and managing TV series data. This project primarily focuses on developing a RESTful API, along with a basic frontend interface for user interaction and authentication.

## Features

- RESTful API for TV series data management
- User authentication system (login and logout)
- Data retrieval and storage for TV series information
- Frontend interface mimicking Netflix's design (home and login pages)

## Technology Stack

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

## Backend

The backend of Notflix is built using Django and Django REST Framework, providing a RESTful API for managing TV series data. Key features include:

- API endpoints for retrieving, storing, and managing TV series information
- User authentication and authorization
- Database integration with MySQL for efficient data storage and retrieval

## Frontend

The frontend of Notflix provides a basic user interface similar to Netflix. It includes:

- A home page with a Netflix-like layout
- A login page for user authentication with a Netflix-like layout

## API Documentation

Swagger UI is used to provide interactive API documentation. After starting the server, access the complete API documentation at:

```
http://localhost/api/swagger/ #docker
http://localhost:8000/api/swagger/ #local
```

Alternatively, you can use the ReDoc version:

```
http://localhost/api/redoc/ #docker
http://localhost:8000/api/redoc/ #local
```

These documents offer detailed information on all available endpoints, request/response formats, and functionality to test the APIs.

## Setup and Usage

This project offers two methods for setup and deployment:
1. Docker Deployment with Nginx (Recommended)
2. Local Setup

### 1. Docker Deployment with Nginx (Recommended)

#### Prerequisites
- Docker and Docker Compose installed on your system

#### Steps
1. Clone the repository:
   ```
   git clone https://github.com/stevenhu19817/notflix.git
   ```

2. Set up environment variables:
    - Copy the `.env.example` file to `.env`:
    ```
    cp .env.example .env
    ```
    - Edit the `.env` file and fill in your actual values for each variable.
   > Note: Obtain the AUTHORIZATION_TOKEN from the TMDB API website.

3. Build and run the Docker containers:
   ```
   docker-compose up --build -d
   ```

4. Run database migrations:
   ```
   docker-compose exec web python manage.py migrate
   ```

Nginx is configured to serve the application and handle static files.<br>
The application will be available at `http://localhost/`.

### 2. Local Setup

#### Prerequisites
- Python 3.10 or higher installed
- MySQL installed

#### Steps
1. Clone the repository:
   ```
   git clone https://github.com/stevenhu19817/notflix.git
   cd notflix
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy the `.env.example` file to `.env.local`:
    ```
    cp .env.example .env.local
    ```
   - Edit the `.env.local` file and fill in your actual values for each variable.
   > Note: Obtain the AUTHORIZATION_TOKEN from the TMDB API website.

5. Set up the database:
   - Create a new MySQL database for the project

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Collect static files:
   ```
   python manage.py collectstatic --no-input
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`.
