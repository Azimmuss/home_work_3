import flet as ft 
from datetime import datetime

def main(page:ft.Page):
    page.title = "Мое приложение"
    greetinng_text = ft.Text("Hello World")

    history_name = []
    history_text = ft.Text('История приветствий')

    name_input = ft.TextField(label="Введите имя")

    def on_button_click(_):
        name = name_input.value.strip()

        timestamp = datetime.now().strftime('%H:%M')
        if name:
             greetinng_text.value = f"{timestamp} Hello {name}"
             name_input.value = ''

             history_name.append(f'{timestamp} - {name}')
             history_text.value = f'История приветствий: \n' + '\n'.join(history_name)
        else:
            greetinng_text.value = "Введите корректное имя"
            greetinng_text.color = ft.Colors.RED    
      
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click) 
    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)

    page.add(greetinng_text, name_input, name_button, history_text)





ft.app(target=main)

