#
# Name: Dawid Nalepa
# ID: 2209302
#

from fastapi import FastAPI, Form
import statistics

app = FastAPI()

@app.post("/api/factorial")
async def factorial(number : str = Form()):
    number = int(number)
    if number <= 0:
        return {"status": 0,
                "message": "Cannot divide by zero!"}
    result = 1
    for i in range(2, number + 1):
        result *= i
    return {"status": 1,
            "parameter": number,
            "action": "factorial",
            "result": result}
        
@app.post("/api/median")
async def median(numbers : str = Form()):
    if not numbers:
        return {"status": 0,
                "message": "Input string is empty"}
    numbers = [int(num) for num in numbers.split(",")]
    if len(numbers) < 2:
        return {"status": 0,
                "message": "Input must contain at least two numbers!"}
   
    median = statistics.median(numbers)
    return {"status": 1,
            "parameter": numbers,
            "action": "median",
            "result": median}

@app.post("/api/variance")
async def variance(numbers : str = Form()):
    if not numbers:
        return {"status": 0,
                "message": "Input string is empty"}
    numbers = [float(num) for num in numbers.split(",")]
    if len(numbers) < 2:
        return {"status": 0,
                "message": "Input must contain at least two numbers!"}
    variance = statistics.pvariance(numbers)
    return {"status": 1,
            "parameter": numbers,
            "action": "variance",
            "result": variance}

@app.post("/api/pstdev")
async def pstdev(numbers : str = Form()):
    if not numbers:
        return {"status": 0,
                "message": "Input string is empty"}
    numbers = [float(num) for num in numbers.split(",")]
    if len(numbers) < 2:
        return {"status": 0,
                "message": "Input must contain at least two numbers!"}
    pstdev = statistics.pstdev(numbers)
    return {"status": 1,
            "parameter": numbers,
            "action": "standard deviation",
            "result": pstdev}
