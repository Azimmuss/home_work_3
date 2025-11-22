import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое приложение"

    greeting_text = ft.Text("Hello World")

    history_name = []
    history_text = ft.Text("История приветствий:")

    name_input = ft.TextField(label="Введите имя")
    age_input = ft.TextField(label="Введите возраст")

    def on_button_click(_):
        name = name_input.value.strip()
        age_str = age_input.value.strip()

        if not name:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED
            page.update()
            return

        if not age_str:
            greeting_text.value = "Пожалуйста введите возраст"
            greeting_text.color = ft.Colors.RED
            page.update()
            return

        if not age_str.isdigit():
            greeting_text.value = "Возраст должен состоять из цифр"
            greeting_text.color = ft.Colors.RED
            page.update()
            return

        age = int(age_str)

        timestamp = datetime.now().strftime("%H:%M")
        greeting_text.value = f"{timestamp} Привет, {name}, тебе {age} лет!"
        greeting_text.color = ft.Colors.BLACK

        name_input.value = ""
        age_input.value = ""

        history_name.append(f"{timestamp} - {name} ({age} лет)")
        history_text.value = "История приветствий:\n" + "\n".join(history_name)

        page.update()

    def delete_last(_):
        if not history_name:
            history_text.value = "История пуста!"
        else:
            history_name.pop()
            if history_name:
                history_text.value = "История приветствий:\n" + "\n".join(history_name)
            else:
                history_text.value = "История пуста!"
        page.update()

    name_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, on_click=on_button_click)

    delete_button = ft.ElevatedButton("Удалить последнее", icon=ft.Icons.DELETE, on_click=delete_last)

    page.add(
        greeting_text,
        name_input,
        age_input,
        name_button,
        delete_button,
        history_text
    )

ft.app(target=main)
