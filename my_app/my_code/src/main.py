import flet as ft
from screens.home import home_screen  # นำเข้า home_screen

def main(page: ft.Page):
    page.title = "Graduate Tracking System"
    page.bgcolor = "white"
    page.scroll = ft.ScrollMode.ALWAYS

    # โหลด Header + Body (ที่สามารถเลื่อนเนื้อหาได้)
    page.add(home_screen())

    # เพิ่ม CupertinoNavigationBar เป็น App Bar ด้านล่าง
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.WHITE,  # พื้นหลังสีขาว
        inactive_color=ft.Colors.GREY,  # สีไอคอนที่ไม่ถูกเลือก
        active_color=ft.Colors.BLACK,  # สีไอคอนที่ถูกเลือก
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, label="Chat"),
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.NOTIFICATIONS, label="Notifications"),
        ]
    )

    page.update()

ft.app(target=main)
