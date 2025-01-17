import flet as ft

def home_screen():
    return ft.Column(
        [
            # Header Section
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(name="search", color="white", size=24),
                        ft.Container(width=10),  # Spacer
                        ft.Text("Graduate Student Tracking System", size=20, color="white", weight="bold"),
                        ft.Container(width=10),  # Spacer
                        ft.Icon(name="notifications", color="white", size=24),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor="#2C2C2C",
                padding=ft.padding.all(10),
            ),

            # Search Bar Section
            ft.Container(
                content=ft.TextField(hint_text="Search", expand=True),
                padding=ft.padding.symmetric(horizontal=15, vertical=10),
                bgcolor="#F5F5F5",
            ),

            # Progress Section
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(name="check_circle", color="green", size=20),
                        ft.Text("เริ่มต้น", color="black", size=16),
                        ft.Container(width=10),  # Spacer
                        ft.Icon(name="remove_circle", color="orange", size=20),
                        ft.Text("กำลังดำเนินการ", color="black", size=16),
                        ft.Container(width=10),  # Spacer
                        ft.Icon(name="error", color="red", size=20),
                        ft.Text("เสร็จสิ้น", color="black", size=16),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor="#FFC0CB",
                padding=ft.padding.all(10),
            ),

            # Document List Section
            ft.ListView(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Image(src="placeholder.png", width=100, height=100),
                                    alignment=ft.alignment.center,
                                ),
                                ft.Text("แบบฟอร์มขอการเป็นอาจารย์ที่ปรึกษา", size=14, weight="bold"),
                                ft.Text("ความสำเร็จ 0%", size=12, color="gray"),
                                ft.ElevatedButton(
                                    "Download PDF", bgcolor="#FFC0CB", color="white", on_click=lambda e: print("Download PDF")
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        padding=ft.padding.all(15),
                        margin=ft.padding.symmetric(vertical=5),
                        bgcolor="#FFFFFF",
                        border=ft.border.all(color="gray", width=1),
                        border_radius=10,
                    ) for _ in range(8)
                ],
                expand=True,
            ),

            # Navigation Bar Section
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.CHAT, icon_size=30, on_click=lambda e: print("Home")),
                        ft.Container(width=10),  # Spacer
                        ft.IconButton(icon=ft.icons.HOME, icon_size=30, on_click=lambda e: print("Notifications")),
                        ft.Container(width=10),  # Spacer
                        ft.IconButton(icon=ft.icons.NOTIFICATIONS, icon_size=30, on_click=lambda e: print("Settings")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                bgcolor="#FFC0CB",
                padding=ft.padding.all(10),
            ),
        ],
        expand=True,
    )
