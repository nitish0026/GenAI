from fastmcp import FastMCP
from fastapi import FastAPI
import uvicorn

app = FastAPI()
mcp = FastMCP("Demo Server for testing purposes!")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b

@app.post("/sundram/mcp/multiply")
def call_multiply(data: dict = Body(...)):
    return {"result": multiply(data.get("a",0), data.get("b",0))}

@app.get("/")
def home():
    return {"message": "Welcome to the FastMCP Demo Server!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3306)