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
