from fastapi import FastAPI, APIRouter
import uvicorn
from routes import eventParticipationRoutes
from routes import eventRoutes, participantRoutes


app = FastAPI()

app.include_router(eventRoutes.router)
app.include_router(participantRoutes.router)
app.include_router(eventParticipationRoutes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
