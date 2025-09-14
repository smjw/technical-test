# WithMe Django/React project
A simple web application allowing users to register, log in, and see a success page. Built with a Django backend and a React frontend.

---

## Features

- User registration (username, email, password, date of birth, city).  
- User login with validation.  
- Simple frontend navigation/pages: Home, Register, Login, Success page.  
- Backend API tested with unit tests.  

--- 

## Tech Stack

- Backend: Django, Django REST Framework, django-cors-headers  
- Frontend: React, React Router  
- Database: SQLite  
- Python version: 3.11.9  
- Node.js version: 10.9.3

---

## Project Structure
```text 
withme/
├─ manage.py
├─ withme/ 
│ ├─ settings.py
│ └─ urls.py
├─ register/
│ ├─ models.py
│ ├─ views.py
│ └─ tests.py
├─ frontend/ 
│ ├─ package.json
│ └─ src/
└─ requirements.txt

```

--- 

## Getting Started

The simplest way to get the project is to use GitHub Desktop to clone the repository to your computer. Once cloned you can install dependencies and set up the virtual environment. After that, the React development server should be started to run the frontend. The backend server and frontend will run locally. The backend runs locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/),you can open the frontend in your browser to interact with the app at [http://localhost:3000/](http://localhost:3000/). 

