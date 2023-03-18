from fastapi import FastAPI, Form

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
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        median = numbers[length // 2]
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
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return {"status": 1,
            "parameter": numbers,
            "action": "variance",
            "result": variance}

@app.get("/api/pstdev")
async def pstdev(parameter : str = Form()):
    return {}