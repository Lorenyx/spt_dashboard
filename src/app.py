import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from .spt.stats import is_spt_server_active, get_active_players, get_profiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# TODO: Track uptime when SPT server starts
start_time = time.time()


def get_uptime():
    elapsed = time.time() - start_time
    hours, rem = divmod(elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"


@app.get("/spt-status", response_class=JSONResponse)
def get_spt_status():
    status = is_spt_server_active()
    profiles = get_profiles() if status else []
    players = get_active_players() if status else []
    return {"server_active": status, "profiles": profiles, "active_players": players, "uptime": get_uptime()}


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    status = is_spt_server_active()
    uptime = get_uptime()
    profiles = get_profiles() if status else []
    players = get_active_players() if status else []
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "server_active": status,
        "uptime": uptime,
        "profiles": profiles,
        "players": players
    })
