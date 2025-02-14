import flet as ft

def header_section():
    """ส่วนหัวของแอป"""
    return ft.Container(
        content=ft.Column(
            [
                # แถวบนสุด: ไอคอนโปรไฟล์, โลโก้กลาง, ปุ่ม Logout
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.ACCOUNT_CIRCLE, icon_color="#FF4081", icon_size=40),
                        ft.Container(
                            content=ft.Image(src="assets/logo_siet.png", width=80, height=80),
                            alignment=ft.alignment.center
                        ),
                        ft.IconButton(icon=ft.Icons.LOGOUT, icon_color="#FF4081", icon_size=30),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                # ช่องค้นหา
                ft.Container(
                    content=ft.TextField(
                        hint_text="Search",
                        prefix_icon=ft.Icons.SEARCH,
                        bgcolor="#757575",
                        border_radius=25,
                        height=45
                    ),
                    margin=ft.margin.only(top=10),
                    padding=ft.padding.symmetric(horizontal=20)
                ),
            ]
        ),
        bgcolor="#2C2C2C",  # พื้นหลังสีดำ
        padding=ft.padding.all(15),
        height=150
    )

def document_item(title, progress=0):
    """ฟังก์ชันสร้าง Layout ของแต่ละเอกสาร"""
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="assets/document_placeholder.png", width=100, height=100),
                             alignment=ft.alignment.center),
                ft.Text(title, size=16, weight="bold"),
                ft.Text(f"ความสำเร็จ {progress} %", size=12, color="gray"),
                ft.Row(
                    [
                        ft.Icon(ft.Icons.CHECK_CIRCLE, color="green" if progress >= 0 else "gray", size=24),
                        ft.Container(width=40, height=2, bgcolor="black"),
                        ft.Icon(ft.Icons.RADIO_BUTTON_UNCHECKED, color="pink" if progress >= 50 else "gray", size=24),
                        ft.Container(width=40, height=2, bgcolor="black"),
                        ft.Icon(ft.Icons.RADIO_BUTTON_UNCHECKED, color="pink" if progress == 100 else "gray", size=24),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton("Download PDF", bgcolor="#FF4081", color="white",
                                  on_click=lambda e: print(f"Downloading {title}")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        padding=ft.padding.all(15),
        margin=ft.margin.symmetric(vertical=5),
        bgcolor="white",
        border=ft.border.all(color="gray", width=1),
        border_radius=10
    )

def body_section():
    """ฟังก์ชันสร้างส่วน Body (รายการเอกสาร)"""
    return ft.ListView(
        controls=[
            document_item("แบบขอรับรองการเป็นอาจารย์ที่ปรึกษาวิทยานิพนธ์", progress=0),
            document_item("แบบเสนอบทหัวข้อและเค้าโครงวิทยานิพนธ์", progress=50),
            document_item("แบบนำส่งเอกสารหัวข้อและเค้าโครง", progress=100),
        ],
        expand=True  # ✅ ใช้ expand=True เพื่อให้เนื้อหาเลื่อนลงได้
    )

def app_bar():
    """สร้าง App Bar ที่ด้านล่างสุด"""
    return ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.WHITE,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, label="Chat"),
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.NOTIFICATIONS, label="Notifications"),
        ]
    )

def home_screen():
    """โหลด Header, Body และ App Bar"""
    return ft.Column(
        [
            header_section(),  # **Header อยู่ด้านบนสุด**
            ft.Container(
                content=body_section(),  # ✅ ใช้ `ListView(expand=True)` เพื่อให้สามารถเลื่อนลงได้
                expand=True  # ✅ ใช้ expand=True เพื่อให้มีพื้นที่เลื่อนลง
            ),
            app_bar()  # ✅ เพิ่ม App Bar ที่ด้านล่างสุด
        ],
        expand=True
    )
