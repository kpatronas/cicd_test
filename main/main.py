from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route to add two numbers
@app.get("/add")
async def add_numbers(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}

