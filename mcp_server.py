from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
import uvicorn

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

async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})

app = Starlette(
    routes=[
        Route("/health", endpoint=health, methods=["GET"]),
        Mount("/", app=mcp.sse_app()),
    ]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)