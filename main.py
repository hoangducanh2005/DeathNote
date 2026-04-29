import os
from nicegui import ui
from app.ui_page import DeathNotePage


page = DeathNotePage()
page.create()

ui.run(
    title="DeathNote",
    reload=False,
    port=int(os.getenv("PORT", "8081"))
)