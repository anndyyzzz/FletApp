import flet as ft

def header_section():
    """ส่วนหัวของแอป"""
    return ft.Container(
        content=ft.Column(
            [
                # แถวบนสุด: ไอคอนโปรไฟล์, โลโก้กลาง, ปุ่ม Logout
                ft.Row(
                    [
                        # ไอคอนโปรไฟล์ (ด้านซ้าย)
                        ft.IconButton(
                            icon=ft.Icons.ACCOUNT_CIRCLE,
                            icon_color="#FF4081",
                            icon_size=40
                        ),

                        # โลโก้กลาง
                        ft.Container(
                            content=ft.Image(
                                src="assets/logo_siet.png",
                                width=80,
                                height=80
                            ),
                            alignment=ft.alignment.center
                        ),

                        # ไอคอน Logout (ด้านขวา)
                        ft.IconButton(
                            icon=ft.Icons.LOGOUT,
                            icon_color="#FF4081",
                            icon_size=30
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                # ช่องค้นหา (อยู่ใต้ Header)
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
                # รูปภาพเอกสาร
                ft.Container(
                    content=ft.Image(
                        src="assets/document_placeholder.png",
                        width=100,
                        height=100
                    ),
                    alignment=ft.alignment.center
                ),

                # ชื่อเอกสาร + ความสำเร็จ
                ft.Text(title, size=16, weight="bold"),
                ft.Text(f"ความสำเร็จ {progress} %", size=12, color="gray"),

                # Progress Indicator แบบ 3 จุด
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(
                                name=ft.Icons.CHECK_CIRCLE,
                                color="green" if progress >= 0 else "gray",
                                size=24
                            ),
                            bgcolor="lightgreen" if progress >= 0 else "white",
                            border_radius=50,
                            padding=5
                        ),
                        ft.Container(width=40, height=2, bgcolor="black"),

                        ft.Container(
                            content=ft.Icon(
                                name=ft.Icons.RADIO_BUTTON_UNCHECKED,
                                color="pink" if progress >= 50 else "gray",
                                size=24
                            ),
                            bgcolor="white",
                            border_radius=50,
                            padding=5
                        ),
                        ft.Container(width=40, height=2, bgcolor="black"),

                        ft.Container(
                            content=ft.Icon(
                                name=ft.Icons.RADIO_BUTTON_UNCHECKED,
                                color="pink" if progress == 100 else "gray",
                                size=24
                            ),
                            bgcolor="white",
                            border_radius=50,
                            padding=5
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                # ปุ่ม Download PDF
                ft.ElevatedButton(
                    "Download PDF",
                    bgcolor="#FF4081",  # สีชมพู
                    color="white",
                    on_click=lambda e: print(f"Downloading {title}"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        padding=ft.padding.all(15),
        margin=ft.padding.symmetric(vertical=5),
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
        expand=True  # **ทำให้สามารถเลื่อนเนื้อหาได้**
    )

def home_screen():
    """โหลด Header และ Body"""
    return ft.Column(
        [
            header_section(),  # Header Bar
            body_section()  # ส่วนเนื้อหาที่เลื่อนได้
        ],
        expand=True
    )
