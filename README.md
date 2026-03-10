RoutePilot 

A backend service for calculating and managing routes using geographic coordinates.
RoutePilot provides a REST API that can be used to compute routes, analyze distances, and integrate with map-based applications.

This project was developed as part of a backend engineering portfolio and demonstrates the use of modern Python backend technologies.

📌 Features

Calculate routes between coordinates

RESTful API built with FastAPI

Database integration with SQLAlchemy

SQLite database for local development

Scalable backend architecture

Ready to integrate with map frontends (Leaflet / OpenStreetMap)

🛠 Tech Stack

Backend:

Python

FastAPI

SQLAlchemy

Uvicorn

Database:

SQLite

Tools:

Git

GitHub

Virtual Environment (venv)

📁 Project Structure
RoutePilot/
│
├── app/
│
├── models/
│
├── schemas/
│
├── services/
│
├── database.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/galleazzijuniorsoftwareenginer/RoutePilot.git

Navigate to the project folder:

cd RoutePilot

Create a virtual environment:

python -m venv venv

Activate the environment:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
▶️ Running the Server

Start the FastAPI server:

uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
📚 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
🗺 Example Use Case

RoutePilot can be used to power:

route optimization tools

delivery applications

mapping platforms

mobility services

logistics systems

Example request:

POST /route

Payload:

{
  "start_lat": 34.0522,
  "start_lng": -118.2437,
  "end_lat": 34.0611,
  "end_lng": -118.3089
  System Architecture

RoutePilot follows a modular backend architecture designed to keep the application scalable, maintainable, and easy to extend.

The system is organized into logical layers separating API handling, business logic, and data persistence.

Client (Frontend / Map App)
            │
            │ HTTP Requests
            ▼
        FastAPI API Layer
            │
            │
            ▼
        Service Layer
     (Business Logic)
            │
            │
            ▼
        Data Layer
     (SQLAlchemy ORM)
            │
            ▼
        SQLite Database
Architecture Layers
API Layer (FastAPI)

Responsible for:

handling HTTP requests

validating request data

exposing REST endpoints

returning JSON responses

Main entry point:

main.py
Service Layer

This layer contains the business logic of the application.

Responsibilities:

route calculations

distance computation

route statistics

processing data before database storage

Files:

services/

Example:

route_stats_services.py
Data Layer

Handles persistence and database interaction using SQLAlchemy.

Responsibilities:

database models

queries

object-relational mapping

Files:

models/
database.py
Database

Currently the system uses:

SQLite

Reasons:

simple setup

lightweight

ideal for development and prototyping

Future production versions could migrate to:

PostgreSQL

MySQL

Request Flow

Example request lifecycle:

Client → FastAPI Endpoint → Service Layer → Database → Response

Example:

POST /route

Client sends coordinates

FastAPI validates input

Service calculates route

Database stores route data

API returns result

Scalability Considerations

The architecture allows future improvements such as:

adding a caching layer (Redis)

integrating external routing APIs

containerization with Docker

deployment to cloud infrastructure
}
📈 Future Improvements

Planned features:

Integration with OpenStreetMap routing

Real street-based route calculation

Interactive map frontend using Leaflet

Route optimization algorithms

Deployment to cloud infrastructure

👨‍💻 Author

Junior Software Engineer

GitHub:
https://github.com/galleazzijuniorsoftwareenginer

📄 License

This project is open-source and available for learning and portfolio purposes.
