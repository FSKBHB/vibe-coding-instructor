from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="AI Vibe Coding — Instructor Page")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Design comparison selector page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/design-a", response_class=HTMLResponse)
async def design_a(request: Request) -> HTMLResponse:
    """Design A: Editorial Luxury Landing Page."""
    return templates.TemplateResponse("pages/design_a.html", {"request": request})


@app.get("/design-b", response_class=HTMLResponse)
async def design_b(request: Request) -> HTMLResponse:
    """Design B: Intimate Split-Panel Coaching Layout."""
    return templates.TemplateResponse("pages/design_b.html", {"request": request})


@app.get("/design-c", response_class=HTMLResponse)
async def design_c(request: Request) -> HTMLResponse:
    """Design C: Bold Dashboard / Bento Grid."""
    return templates.TemplateResponse("pages/design_c.html", {"request": request})
