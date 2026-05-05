from flask import Flask, request, jsonify

app = Flask(__name__)


def cheap_flights_recipe(origin, destination, date, budget):
    cheapest_price = 85

    if cheapest_price <= budget:
        recommendation = "Good option within budget"
    else:
        recommendation = "Flight exceeds budget"

    result = {
        "origin": origin,
        "destination": destination,
        "date": date,
        "budget": budget,
        "cheapest_price": cheapest_price,
        "airline": "Example Airline",
        "recommendation": recommendation
    }

    return result

@app.route("/cheap-flights", methods=["GET", "POST"])
def cheap_flights():
    if request.method == "GET":
        return jsonify({
            "message": "Cheap Flights API is working. Use POST to send origin, destination, date and budget."
        })

    data = request.get_json()

    origin = data.get("origin")
    destination = data.get("destination")
    date = data.get("date")
    budget = int(data.get("budget"))

    result = cheap_flights_recipe(origin, destination, date, budget)

    return jsonify(result) 