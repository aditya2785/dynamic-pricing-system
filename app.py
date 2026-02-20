from flask import Flask, request, jsonify
import joblib
import numpy as np

from flask import render_template

from src.optimizer import optimize_prices

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/demand_model.pkl")
scaler = joblib.load("models/demand_scaler.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flight Dynamic Pricing API is running 🚀"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("Raw JSON received:", request.get_data())
        data = request.get_json(force=True)
        print("Parsed JSON:", data)

        features = np.array(data["features"]).reshape(1, -1)
        feature_names = data["feature_names"]

        scaled_features = scaler.transform(features)
        predicted_demand = model.predict(scaled_features)[0]

        optimization_result = optimize_prices(
            model=model,
            scaler=scaler,
            base_features=features,
            feature_names=feature_names
        )

        return jsonify({
            "predicted_demand": float(predicted_demand),
            "optimization": optimization_result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/dashboard")
def dashboard():
    return render_template("main.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
