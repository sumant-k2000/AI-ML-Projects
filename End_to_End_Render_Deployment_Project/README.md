# Student Performance Predictor

A machine learning web application that predicts a student's math score based on demographic and academic inputs. The model is deployed using Flask and hosted on Render.

## Features

- User-friendly web interface
- Machine learning based prediction
- Flask backend API
- Deployed on Render cloud platform

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- HTML/CSS
- Render
  

## Installation & Setup

Clone the repository:

```bash
git clone <repository-url>
cd Student-Performance-Predictor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

## Deployment on Render

1. Push the project to GitHub.
2. Create a new Web Service on Render.
3. Connect the GitHub repository.
4. Configure:

**Build Command**
```
pip install -r requirements.txt
```

**Start Command**
```
gunicorn app:app
```

5. Deploy the application.

## Environment

Python version:

```
3.x
```

## Model

The machine learning model is trained using student performance data and saved as:

```
model.pkl
```

The Flask application loads this model and generates predictions through the web interface.


