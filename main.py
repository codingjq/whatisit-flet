import flet as ft

def main(page: ft.Page):
    hello_world = ft.Text(value="Hello World 😊")

    counter = ft.TextField(value="0")

    def button_clicked(e):
        counter.value = int(counter.value) + 1
        hello_world.value = f"You clicked me {str(counter.value)} times"
        page.update()

    button = ft.TextButton("Click Me", on_click=button_clicked)

    page.add(
        ft.ResponsiveRow(
            [
                hello_world,
                button
            ]
        )
    )

ft.app(target=main)