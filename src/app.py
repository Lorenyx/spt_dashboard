from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from .constants import SPT_SERVER
from .spt.stats import is_spt_server_active

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/spt-status", response_class=JSONResponse)
async def get_spt_status():
    return {"server_active": is_spt_server_active()}


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    status = await is_spt_server_active()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "server_active": status,
        "SPT_SERVER": SPT_SERVER,
    })
