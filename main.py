from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.api import router as api_router
import os

app = FastAPI(title="Learn_Py", description="Learn Python from Zero to OOP", version="1.0.0")

# CORS middleware
# Note: For production, replace ["*"] with specific allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Configure specific origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api", tags=["api"])

# Mount static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main dashboard page"""
    try:
        with open("frontend/templates/index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dashboard page not found")


@app.get("/quizzes", response_class=HTMLResponse)
async def quizzes_page():
    """Serve the quizzes page"""
    try:
        with open("frontend/templates/quizzes.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Quizzes page not found")


@app.get("/flashcards", response_class=HTMLResponse)
async def flashcards_page():
    """Serve the flashcards page"""
    try:
        with open("frontend/templates/flashcards.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Flashcards page not found")


@app.get("/mindmap", response_class=HTMLResponse)
async def mindmap_page():
    """Serve the mind map page"""
    try:
        with open("frontend/templates/mindmap.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Mind map page not found")


@app.get("/progress", response_class=HTMLResponse)
async def progress_page():
    """Serve the progress tracking page"""
    try:
        with open("frontend/templates/progress.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Progress page not found")


@app.get("/learning-path", response_class=HTMLResponse)
async def learning_path_page():
    """Serve the learning path page"""
    try:
        with open("frontend/templates/learning_path.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Learning path page not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
