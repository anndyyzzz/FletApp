import flet as ft
from screens.home import home_screen

def main(page: ft.Page):
    # Set up the main page
    page.title = "Graduate Tracking System"
    page.scroll = ft.ScrollMode.ALWAYS

    # Load the home screen
    page.add(home_screen())

    # Update the UI
    page.update()

# Run the app
ft.app(target=main)
