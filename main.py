from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.api import router as api_router
import os

app = FastAPI(title="Learn_Py", description="Learn Python from Zero to OOP", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    with open("frontend/templates/index.html", "r") as f:
        return f.read()


@app.get("/quizzes", response_class=HTMLResponse)
async def quizzes_page():
    """Serve the quizzes page"""
    with open("frontend/templates/quizzes.html", "r") as f:
        return f.read()


@app.get("/flashcards", response_class=HTMLResponse)
async def flashcards_page():
    """Serve the flashcards page"""
    with open("frontend/templates/flashcards.html", "r") as f:
        return f.read()


@app.get("/mindmap", response_class=HTMLResponse)
async def mindmap_page():
    """Serve the mind map page"""
    with open("frontend/templates/mindmap.html", "r") as f:
        return f.read()


@app.get("/progress", response_class=HTMLResponse)
async def progress_page():
    """Serve the progress tracking page"""
    with open("frontend/templates/progress.html", "r") as f:
        return f.read()


@app.get("/learning-path", response_class=HTMLResponse)
async def learning_path_page():
    """Serve the learning path page"""
    with open("frontend/templates/learning_path.html", "r") as f:
        return f.read()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
