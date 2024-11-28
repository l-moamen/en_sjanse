from fastapi import FastAPI
from app.routers.venue import router as venue_router
from app.routers.performer import router as performer_router

# Initialize FastAPI app
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}


# Include the venue_router for all venue-related routes
app.include_router(venue_router, prefix="/venues", tags=["venues"])
app.include_router(performer_router, prefix="/performers", tags=["venues"])
