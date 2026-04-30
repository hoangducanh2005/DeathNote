import os
from pathlib import Path
from nicegui import ui, app as nicegui_app
from app.ui_page import DeathNotePage

BASE_DIR = Path(__file__).parent

nicegui_app.add_static_files(
    "/res",
    BASE_DIR / "app" / "res"
)

page = DeathNotePage()
page.create()

ui.run(
    title="DeathNote",
    reload=False,
    port=int(os.getenv("PORT", "8081"))
)