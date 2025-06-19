from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/getFlightStatus")
def get_flight_status(
    pnr: str = Query(..., min_length=6, max_length=6, pattern="^[A-Z0-9]{6}$"),
    lastName: str = Query(..., min_length=2)
):
    return JSONResponse({
        "pnr": pnr,
        "last_name": lastName,
        "airline": "American Airlines",
        "flight_number": "AA1234",
        "departure": "JFK",
        "arrival": "LAX",
        "departure_time": "2025-06-20T09:00:00",
        "arrival_time": "2025-06-20T12:00:00",
        "status": "On Time"
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
