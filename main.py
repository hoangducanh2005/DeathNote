import os
from nicegui import ui
from app.ui_page import DeathNotePage

ui.add_static_files("/res", "app/res")

page = DeathNotePage()
page.create()

ui.run(
    title="DeathNote",
    reload=False,
    port=int(os.getenv("PORT", "8081"))
)