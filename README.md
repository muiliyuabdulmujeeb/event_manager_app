# Event Management API

A FastAPI-based system for managing events, user registrations, attendance, and speaker details. This system allows users to register for events, track attendance, and manage both event information and speaker details. It supports CRUD operations and enforces simple validation and relationships between the entities.



## Table of Contents

- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Application](#running-the-application)  
- [API Documentation](#api-documentation)  
  - [Usage Example](#usage-example)  
- [Project Structure](#project-structure)  
- [Validation & Business Rules](#validation--business-rules)   
- [Contact](#contact)  

## Features

- User registration  
- Event creation, update, deletion, and listing  
- Speaker management and assignment to events  
- User event registration and attendance tracking    
- RESTful API design with automatic documentation via Swagger UI  

## Getting Started

### Prerequisites

- Python 3.8+  
- pip (Python package manager)  

### Installation

```bash
git clone https://github.com/muiliyuabdulmujeeb/event_manager_app.git
cd event_manager_app
python -m venv venv (install a virtual environmant called venv)
venv\Scripts\activate (activate venv on windows)
source venv/bin/activate (activate venv on Linux or macos)
pip install fastapi uvicorn
pip install pydantic
```

### Running the Application

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

## API Documentation

The API is documented using Swagger UI. Key endpoints include:

| Method | Endpoint                        | Description                         |
|--------|---------------------------------|-------------------------------------|
| GET    | `/speaker/`                     | List initialized speakers           |
| GET    | `/user/all`                     | List all users                      |
| POST   | `/user/`                        | Create a new user                   |
| PATCH  | `/user/`                        | Update user                         |
| GET    | `/user/{user_id}`               | Retrieve user details               |
| DELETE | `/user/{user_id}`               | Delete user                         |
| PATCH  | `/user/{user_id}/deactivate`    | Deactivate user                     |
| GET    | `/event/`                       | List all events                     |
| POST   | `/event/`                       | Create a new event                  |
| PATCH  | `/event/`                       | Update event                        |
| GET    | `/event/{event_id}`             | Retrieve event details              |
| PATCH  | `/event/{event_id}/close`       | close registration for an event     |
| DELETE | `/event/{event_id}`             | Delete event                        |
| GET    | `/event/eventspeaker`           | List all event speakers             |
| POST   | `/event/eventspeaker`           | Create a new event speaker          |
| POST   | `registration/register`         | Register user for event             |
| GET    | `/registration/all`             | List all registrations              |
| PATCH  | `/registration/{reg_id}/attend` | Mark event attendance for a user    |

See [http://localhost:8000/docs](http://localhost:8000/docs) for the full list and detailed API specs.

### Usage Example

#### Example: Registering a User for an Event

**Request:**

```curl -X 'POST' \
  'http://localhost:8000/registration/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "07a31ba1-98a7-4daf-85ea-21386db7207c",
  "event_id": "84b2337e-78f7-462a-ba24-e7f6dd68fd1b",
  "reg_date": "2025-07-12"
}'
```

**Response:**

```json
{
  "id": "78d39036-aad9-4d06-9a2a-f9a927fb32ea",
  "user_id": "07a31ba1-98a7-4daf-85ea-21386db7207c",
  "event_id": "84b2337e-78f7-462a-ba24-e7f6dd68fd1b",
  "reg_date": "2025-07-12",
  "attended": false
}
```


## Project Structure

```
event_manager_app/
├── main.py
├── models.py
├── routes/
│   ├── event.py
│   ├── registration.py
│   ├── speaker.py
│   └── user.py
├── schemas/
│   ├── event.py
│   ├── registration.py
│   ├── speaker.py
│   └── user.py
├── services/
│   ├── event.py
│   ├── registration.py
│   ├── speaker.py
│   └── user.py
├── .gitignore
├── database.py
└── README.md
```

## Validation & Business Rules

- Users cannot register for the same event more than once.  
- Only active users can register for events.  
- Event must be open for user to register.
- Speakers must be initialized using the `/speaker/` endpoint to get speaker_id .  
- Attendance can only be marked for registered users.  



## Contact

Creator: Muiliyu Abdul-mujeeb
Altschool ID: ALT/SOE/024/5573  
Email: muiliyuabdulmujeeb@gmail.com  
GitHub: [muiliyuabdulmujeeb](https://github.com/muiliyuabdulmujeeb)
