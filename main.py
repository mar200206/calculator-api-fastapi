from fastapi import FastAPI, HTTPException
from app.services import calculate
from app.storage import save_record, get_history

app = FastAPI()

@app.post('/calculate')
def calc(a: float, b: float, operation: str):
    try:
        result = calculate(a, b, operation)
        save_record(a, b, operation, result)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/history')
def history():
    return get_history()
