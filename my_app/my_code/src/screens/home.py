import flet as ft

def home_screen():
    return ft.Column(
        [
            # Header Section (Placeholder)
            ft.Container(
                content=ft.Text("Graduate Tracking System", size=30, weight="bold", color="white"),
                bgcolor="blue",
                padding=20,
                alignment=ft.alignment.center,
            ),

            # Welcome Text Section
            ft.Container(
                content=ft.Text("ยินดีต้อนรับสู่ระบบติดตามสถานะนักศึกษา", size=24, weight="bold"),
                alignment=ft.alignment.center,
                padding=20,
                bgcolor="lightblue",
            ),

            # Buttons Section
            ft.Container(
                content=ft.Column(
                    [
                        ft.ElevatedButton("เข้าสู่ระบบ", on_click=lambda e: print("ไปที่หน้าล็อกอิน")),
                        ft.ElevatedButton("โปรไฟล์", on_click=lambda e: print("ไปที่หน้าโปรไฟล์")),
                        ft.ElevatedButton("ติดต่อเจ้าหน้าที่", on_click=lambda e: print("ไปที่หน้าติดต่อเจ้าหน้าที่")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                padding=20,
            ),

            # Footer Section (Placeholder)
            ft.Container(
                content=ft.Text("© 2025 Graduate Tracking System", size=12, color="gray"),
                padding=10,
                alignment=ft.alignment.center,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )
