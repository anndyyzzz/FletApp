import flet as ft

def signin_screen(page: ft.Page):
    """สร้างหน้า Sign In"""
    def go_to_home(e):
        page.go("/home")  # ไปยังหน้า Home เมื่อกดปุ่ม Sign In

    return ft.Column(
        [
            # โลโก้หลัก
            ft.Container(
                content=ft.Image(src="assets/logo_siet.png", width=100, height=100),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=50)
            ),

            # โลโก้ SIET | KMITL
            ft.Container(
                content=ft.Image(src="assets/kmitl.png", width=200, height=80),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=20, bottom=30)
            ),

            # ปุ่ม Sign In
            ft.Container(
                content=ft.ElevatedButton(
                    "Sign in",
                    bgcolor="#FF76A6",
                    color="white",
                    on_click=go_to_home,  # กดแล้วไปหน้า Home
                    width=150,
                    height=40,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                ),
                alignment=ft.alignment.center,
            ),

            # ชื่อระบบ
            ft.Container(
                content=ft.Text(
                    "Graduate Student Tracking System\nMobile Application",
                    size=14, weight="bold", color="#FF4081", text_align=ft.TextAlign.CENTER, italic=True
                ),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=20)
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
