import flet as ft
from screens.signin import signin_screen
from screens.home import home_screen

def route_change(event: ft.RouteChangeEvent):
    """กำหนดเส้นทางเปลี่ยนหน้า"""
    page = event.page  # ดึง `page` จาก Event
    page.clean()  # ล้างเนื้อหาก่อนเปลี่ยนหน้า
    
    if page.route == "/":
        page.add(signin_screen(page))  # ส่ง `page` เข้า `signin_screen()`
    elif page.route == "/home":
        page.add(home_screen())  # โหลดหน้า Home

def main(page: ft.Page):
    page.title = "Graduate Student Tracking System"
    page.bgcolor = "white"  # ✅ ตั้งค่าพื้นหลังเป็นสีขาว
    page.on_route_change = route_change  # ตรวจจับการเปลี่ยนหน้า
    page.go("/")  # เปิดแอปที่หน้า Sign In

ft.app(target=main)
