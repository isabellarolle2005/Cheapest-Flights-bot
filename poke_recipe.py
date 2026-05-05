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


origin = input("From: ")
destination = input("To: ")
date = input("Date (YYYY-MM-DD): ")
budget = int(input("Budget (€): "))

recipe_result = cheap_flights_recipe(
    origin,
    destination,
    date,
    budget
)

print("\n--- CHEAP FLIGHTS RESULT ---")
print(f"Route: {recipe_result['origin']} → {recipe_result['destination']}")
print(f"Date: {recipe_result['date']}")
print(f"Budget: €{recipe_result['budget']}")
print(f"Cheapest price found: €{recipe_result['cheapest_price']}")
print(f"Airline: {recipe_result['airline']}")
print(f"Recommendation: {recipe_result['recommendation']}") 