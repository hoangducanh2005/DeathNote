# this file is for learning and testing the nicegui library, 
# which is a Python library for building web applications with a simple and intuitive API. 
# The code creates a basic web page with a label, a link to a portfolio, 
# two chat messages, and an HTML snippet demonstrating text formatting and a hyperlink. 
# Finally, it runs the application to display the web page.

import os
import app.res
from pathlib import Path
from nicegui import ui,app as nicegui_app
from app.storage import BASE_DIR

nicegui_app.add_static_files(
    '/res',
    BASE_DIR / 'app' / 'res'
)

ui.label("Hello, world! my name is hda")

ui.link("Visit my Portfolio", 
        "https://hoangducanh2005.github.io/Portfolio/",
        new_tab=True
) 

ui.chat_message(
    "Hello there, my name is HDA and what's your name?",
    name = "HDA",
    stamp= "now",   #time
    avatar="https://avatars.githubusercontent.com/u/122863441?v=4"
)

ui.chat_message(
    "Hello there, my name is HDA and what's your name?",
    name = "HDA",
    stamp= "now",   #time
    avatar="https://avatars.githubusercontent.com/u/122863441?v=4"
)

ui.button("Click me",color="purple", on_click=lambda: ui.notify("Button clicked!"))
ui.button("Hit me",color="red", on_click=lambda: ui.link("this is my channel",
                                             "https://www.youtube.com/watch?v=u4-VTXwmYvM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=3")
          )

gender_image = ui.image('/res/man.png').classes('w-48')
radio_image  = ui.image('/res/woman.webp').classes('w-48')

ui.switch("Nihongo")

ui.run()