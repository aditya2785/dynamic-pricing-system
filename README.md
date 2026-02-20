Dynamic Pricing Optimization System built using XGBoost and regression modeling to forecast demand, simulate price elasticity, and maximize profit using a custom optimization engine. Packaged as a Flask REST API and containerized with Docker for scalable deployment.

📌 What It Does
Predicts flight ticket demand using machine learning
Simulates price elasticity
Optimizes price to maximize:
(Price−Cost)×Demand
Provides an interactive dashboard
Fully containerized using Docker

🧠 Tech Stack
Python
XGBoost
Scikit-learn
Flask
Docker

🏗 Project Structure
src/
 ├── data_gen.py      # Data preprocessing
 ├── train.py         # Model training
 ├── optimizer.py     # Profit optimization
templates/
 └── main.html        # Dashboard UI
app.py                # Flask API
Dockerfile

⚙️ Run Locally
Train model:
python -m src.train
Start app:
python app.py

Open:
http://127.0.0.1:5000/dashboard

🎯 Key Highlights
Demand forecasting with R² evaluation
Multi-price scenario simulation
Profit-maximization engine
REST API + Dashboard
Docker-ready deployment
