from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/api/factioral")
async def factorial(number : str = Form()):
    number = int(number)
    if number <= 0:
        return {"status": 0,
                "message": "Cannot divide by zero"}
    result = 1
    for i in range(2, number + 1):
        result *= i
    try:
        return {"status": 1,
                "parameter": number,
                "action": "factorial",
                "result": result}
    except Exception as e:
        return {"status": 0,
                "message": e}
        
@app.post("/api/median")
async def median(parameter : str = Form()):
    return {}

@app.post("/api/variance")
async def variance(parameter : str = Form()):
    return {}

@app.get("/api/pstdev")
async def pstdev(parameter : str = Form()):
    return {}