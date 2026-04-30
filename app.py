# this file is for learning and testing the nicegui library, 
# which is a Python library for building web applications with a simple and intuitive API. 
# The code creates a basic web page with a label, a link to a portfolio, 
# two chat messages, and an HTML snippet demonstrating text formatting and a hyperlink. 
# Finally, it runs the application to display the web page.

import os

from nicegui import ui

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



ui.run()