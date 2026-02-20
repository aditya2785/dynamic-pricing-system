Dynamic Pricing Optimization System built using XGBoost and regression modeling to forecast demand, simulate price elasticity, and maximize profit using a custom optimization engine. Packaged as a Flask REST API and containerized with Docker for scalable deployment.
This project implements an end-to-end Dynamic Pricing Optimization System for flight ticket pricing using machine learning and profit maximization logic.
The system predicts ticket demand using XGBoost, estimates price elasticity through scenario simulation, and determines the optimal price that maximizes profit using a custom optimization engine.

It includes:

Demand forecasting model

Profit maximization algorithm

Flask REST API

Interactive dashboard

Docker containerization for deployment

🧠 Problem Statement

Airline pricing must dynamically adjust based on:

Time before departure

Flight duration

Stop type

Time of day

Customer demand sensitivity

The objective is to:

Maximize
 
Profit
=
(
𝑃
𝑟
𝑖
𝑐
𝑒
−
𝐶
𝑜
𝑠
𝑡
)
×
𝐷
𝑒
𝑚
𝑎
𝑛
𝑑
Maximize Profit=(Price−Cost)×Demand

Instead of static pricing, this system dynamically determines the optimal ticket price.

🏗️ System Architecture
EDA Notebook
     ↓
Data Pipeline (data_gen.py)
     ↓
Demand Model Training (train.py)
     ↓
Optimization Engine (optimizer.py)
     ↓
Flask API (app.py)
     ↓
Dashboard + Docker Deployment
🔍 Features
1️⃣ Demand Forecasting

XGBoost Regressor

K-Fold Cross Validation

RMSE and R² evaluation

Feature importance analysis

2️⃣ Price Elasticity Simulation

Multi-price scenario testing

Demand sensitivity modeling

Revenue impact evaluation

3️⃣ Profit Maximization Engine

Optimizes:

(Price−Cost)×Demand

Searches price range dynamically

Identifies profit-maximizing price

Compares against static pricing

4️⃣ Interactive Dashboard

User inputs flight parameters

Displays:

Predicted demand

Optimal price

Expected demand

Maximum profit

5️⃣ Dockerized Deployment

Fully containerized

Ready for cloud deployment (Render / AWS)

🛠️ Tech Stack

Python

XGBoost

Scikit-learn

Flask

NumPy / Pandas

Docker

HTML / CSS (Dashboard)

📂 Project Structure
dynamic-pricing-system/
│
├── src/
│   ├── data_gen.py        # Data preprocessing pipeline
│   ├── train.py           # Model training script
│   ├── optimizer.py       # Profit optimization logic
│
├── templates/
│   └── main.html          # Dashboard UI
│
├── models/
│   ├── demand_model.pkl
│   └── demand_scaler.pkl
│
├── app.py                 # Flask API
├── Dockerfile
├── requirements.txt
└── README.md
⚙️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Train the model
python -m src.train
3️⃣ Start the API
python app.py

Visit:

http://127.0.0.1:5000/dashboard
🐳 Run with Docker
Build Image
docker build -t flight-pricing .
Run Container
docker run -p 5000:5000 flight-pricing

Open:

http://localhost:5000/dashboard
📊 Example Output

Predicted Demand: 28.48

Optimal Price: ₹6500

Expected Demand: 28.48

Max Profit: ₹71,201

📈 Model Insights

Key demand drivers identified through feature importance:

Stop type

Price

Days before flight

Departure time

Arrival category
