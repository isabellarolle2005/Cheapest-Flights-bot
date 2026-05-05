import os
from mcp.server.fastmcp import FastMCP

os.environ["HOST"] = "0.0.0.0"
os.environ["PORT"] = os.environ.get("PORT", "8000")

mcp = FastMCP(
    name="Cheap Flights Finder",
    instructions="Find cheap flight recommendations using origin, destination, date and budget."
)

if __name__ == "__main__":
    mcp.run(transport="sse")