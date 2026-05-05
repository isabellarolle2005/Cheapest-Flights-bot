import os
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))

mcp = FastMCP(
    name="Cheap Flights Finder",
    instructions="Find cheap flight recommendations using origin, destination, date and budget.",
    host="0.0.0.0",
    port=port
)

mcp = FastMCP(
    name="Cheap Flights Finder",
    instructions="Find cheap flight recommendations using origin, destination, date and budget."
)


@mcp.tool()
def find_cheap_flight(origin: str, destination: str, date: str, budget: int) -> dict:
    """
    Find the cheapest flight recommendation based on origin, destination, date and budget.
    """

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
    mcp.run(transport="sse")