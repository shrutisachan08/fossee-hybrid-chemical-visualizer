# CSV Dashboard Web App

A web-based dashboard for uploading CSV files containing chemical equipment data. Users can view summaries, generate charts, track dataset history, and download PDF reports. Built with **React** for the frontend and **Django** for the backend.

# Features

* **CSV Upload** – Upload CSV files easily.
* **Latest Dataset Overview** – View the most recently uploaded dataset.
* **Data Summary** – Quick summary of uploaded data.
* **Charts & Visualizations** – Explore dataset trends visually.
* **Dataset History** – Browse past uploads with timestamps.
* **PDF Report Download** – Download a PDF version of the dataset summary.
* **User Authentication** – Logout functionality included.

# Demo Credentials

You can test the app using these credentials:

* **Username:** `demo`
* **Password:** `demo123`

# Tech Stack

* **Frontend:** React, JavaScript, HTML, CSS
* **Backend:** Django REST Framework, Python
* **API:** Axios for frontend-backend communication
* **Styling:** Custom CSS with responsive design

# Installation & Setup

## Backend (Django)

```bash
# Clone the repository
git clone https://github.com/yourusername/csv-dashboard.git
cd csv-dashboard/backend

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the backend server
python manage.py runserver
```

## Frontend (React)

```bash
cd ../web-frontend
npm install
npm start
```

## Desktop
```bash
cd ../desktop-app
python manage.py
``` 

Open your browser at [http://localhost:3000](http://localhost:3000)

# Usage

1. Login using **demo / demo123**.
2. Upload a CSV file using the **+ Upload CSV** button.
3. View the latest dataset summary, charts, and history.
4. Download a PDF report using the **Download** button.
5. Logout using the **Logout** button.

# Folder Structure

```
backend/                 # Django backend
  ├─ api/                # Django app for CSV APIs
  ├─ manage.py
frontend/                # React frontend
  ├─ src/
      ├─ components/     # Summary, Charts, DatasetHistory, PDFReport
      ├─ Pages/          # Dashboard, Login, Home
      ├─ api/            # Axios API setup
      ├─ App.js
      ├─ dashboard.css
```

