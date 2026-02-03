# Fossee-hybrid-chemical-visualizer

This project is a **Web + Desktop Equipment Dashboard** that allows users to upload CSV files, analyze equipment data, visualize results using charts, and view dataset history.

The system consists of three main parts:

* **Backend Server** – Handles CSV processing and APIs
* **Web Frontend** – Browser-based dashboard for visualization
* **Desktop App** – PyQt-based desktop visualizer

---

# Project Structure

```
Equipment-Dashboard/
│
├─ backend/
│   ├─ server/           # Backend server logic (API, CSV processing)
│   ├─ visualizer/       # Backend-side visualization / analysis utilities
│
├─ web-frontend/
│   ├─ src/
│   │   ├─ components/   # Reusable React components
│   │   ├─ pages/        # Page-level components (Dashboard, Login, etc.)
│   │   ├─ styles/       # CSS files for styling
│   │   ├─ api/          # Axios API configuration
│   │   ├─ App.js        # Main React app
│   │   ├─ index.js      # React entry point
│
├─ desktop-app/
│   ├─ charts.py         # Chart rendering logic
│   ├─ api.py            # API communication with backend
│   ├─ main.py           # Desktop application entry point
│
└─ README.md
```

---

# Features

* Upload CSV files containing equipment data
* Automatic data analysis on upload
* Summary statistics and charts
* Dataset history tracking
* Web-based dashboard (React)
* Desktop-based visualization app (Python)

---

# Demo Credentials (Web App)

Use the following credentials to test the web dashboard:

* **Username:** `demo`
* **Password:** `demo123`

---

# Setup Instructions

## Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Start backend server
python manage.py runserver
```

> Make sure the backend server is running before starting the web or desktop app.

---

## Web Frontend Setup

```bash
cd web-frontend
npm install
npm start
```

Open the browser at:

```
http://localhost:3000
```

---

## Desktop App Setup

```bash
cd desktop-app
python main.py
```

The desktop app connects to the backend API to fetch data and display charts.

---

# Usage

1. Start the backend server
2. Login to the web dashboard using **demo / demo123**
3. Upload a CSV file
4. View summaries, charts, and dataset history
5. Optionally launch the desktop app for visualization

---

# Notes

* Frontend and backend are deployed independently and communicate via APIs
* The desktop app uses the same backend APIs as the web frontend
* Ensure CORS is enabled on the backend for frontend access

---



