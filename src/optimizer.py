import numpy as np

def optimize_prices(model, scaler, base_features, feature_names, cost=4000):

    price_index = feature_names.index("Price")

    best_profit = -np.inf
    best_price = None
    best_demand = None

    original_price = base_features[0][price_index]

    price_range = np.linspace(original_price * 0.8,
                              original_price * 1.3,
                              30)

    for p in price_range:

        test_features = base_features.copy()
        test_features[0][price_index] = p

        scaled = scaler.transform(test_features)
        predicted_demand = model.predict(scaled)[0]

        profit = (p - cost) * predicted_demand

        if profit > best_profit:
            best_profit = profit
            best_price = p
            best_demand = predicted_demand

    return {
        "optimal_price": float(best_price),
        "expected_demand": float(best_demand),
        "max_profit": float(best_profit)
    }