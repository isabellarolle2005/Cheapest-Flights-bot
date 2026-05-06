from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Cheap Flights Finder",
    instructions="Find cheap flight recommendations using origin, destination, date and budget."
)

@mcp.tool()
def find_cheap_flight(origin: str, destination: str, date: str, budget: int) -> dict:
    cheapest_price = 85

    if cheapest_price <= budget:
        recommendation = "Good option within budget"
    else:
        recommendation = "Flight exceeds budget"

    return {
        "origin": origin,
        "destination": destination,
        "date": date,
        "budget": budget,
        "cheapest_price": cheapest_price,
        "airline": "Example Airline",
        "recommendation": recommendation
    }

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)