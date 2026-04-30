from nicegui import ui,app as nicegui_app
import os

ui_name = ui.input(label='Name',
                   placeholder = 'Enter your name')
ui_message = ui.textarea(label='Message',
                    placeholder = 'Enter your message')
button = ui.button('Send',color='purple',on_click=lambda: send())

def send():
    
    ui.chat_message(
        f'{ui_message.value}',
        name=f'{ui_name.value}',
        stamp='now',
        avatar='https://avatars.githubusercontent.com/u/122863441?v=4' 
    )
    
    ui_name.value = ''
    ui_message.value = ''   
ui.run()