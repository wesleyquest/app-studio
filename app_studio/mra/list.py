import reflex as rx
#
from .state import MRAState
from .. import navigation
from ..ui import dashboard_page
#
#
def custom_file_upload() -> rx.Component:
    return rx.upload.root(
    rx.box(
        rx.icon(
            tag="cloud_upload",
            style={
                "width": "3rem",
                "height": "3rem",
                "color": "#2563eb",
                "marginBottom": "0.75rem",
            },
        ),
        rx.hstack(
            rx.text(
                "여기에 파일을 업로드해 주세요",
                size="4",
            ),
        ),
        rx.text(
            "확장자가 PDF(.pdf)인 파일 1개씩 업로드 가능",
            color_scheme="red",
            size="3",
            style={
                "marginTop": "0.5rem",
            },
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "1.5rem",
            "textAlign": "center",
        },
    ),
    id="my_upload",
    style={
        # "maxWidth": "24rem",
        #"width": "100%",
        "width": "800px",
        "height": "12rem",
        "borderWidth": "2px",
        "borderStyle": "dashed",
        "borderColor": "#60a5fa",
        "borderRadius": "0.75rem",
        "cursor": "pointer",
        "transitionProperty": "background-color",
        "transitionDuration": "0.2s",
        "transitionTimingFunction": "ease-in-out",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        #"boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
        "_hover": {
            "cursor": "pointer",
            "bg": rx.color("accent", 4),
        },
    },
    box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px",
    # rx.upload.root prop
    max_files=1,
    accept={
        "application/pdf": [".pdf"]
    }
    )


def file_upload_v1() -> rx.Component:
    return rx.vstack(
        rx.cond(
            rx.selected_files("my_upload").length() > 0,
            rx.vstack(
                rx.image(src="/pdf_icon.png", width="40px"),
                rx.foreach(
                    rx.selected_files("my_upload"), rx.text
                ),
            rx.cond(
                MRAState.uploading | MRAState.running,
                rx.fragment(),
                rx.hstack(
                    rx.button(
                        "Upload",
                        on_click=MRAState.handle_upload(
                            rx.upload_files(
                                upload_id="my_upload",
                                on_upload_progress=MRAState.handle_upload_progress,
                            ),
                        ),
                        size="3",
                    ),
                    rx.button(
                        "Cancel",
                        on_click=MRAState.cancel_file,
                        size="3",
                        variant="outline",
                    ),
                    align="center",
                    padding_top="10px",
                )
            ),
            style={
                # "maxWidth": "24rem",
                #"width": "100%",
                "width": "800px",
                "height": "12rem",
                "borderWidth": "2px",
                "borderStyle": "dashed",
                "borderColor": "#60a5fa",
                "borderRadius": "0.75rem",
                #"cursor": "pointer",
                "transitionProperty": "background-color",
                "transitionDuration": "0.2s",
                "transitionTimingFunction": "ease-in-out",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
            }                
            ),
            custom_file_upload(),            
        ),
        # extraction
        rx.cond(
            MRAState.uploading | MRAState.running,
            rx.progress(value=MRAState.progress, max=100),
        ),
        rx.cond(
            MRAState.uploading | MRAState.running,
            rx.button(
                "Cancel",
                on_click=MRAState.cancel_running,
            ),
        ),
        align="center",
    )

def file_item(file):
    wonbu_no = MRAState.wonbu_no_var
    file_name = file["name"]
    file_ext = file["ext"]
    file_url = rx.get_upload_url("") + f"/mra/{wonbu_no}/{file_name}.{file_ext}"
    return rx.box(
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            rx.image(src="/pdf_icon.png", width="30px"),
                            rx.text(f"{file["name"]}.{file["ext"]}"),
                            align="center",
                        ),
                        width="50%",
                    ),
                    rx.box(
                        rx.text(file["datetime"]),
                        text_align="center",
                        width="20%"
                    ),
                    rx.box(
                        rx.text(file["size"]),
                        text_align="center",
                        width="15%"
                    ),                        
                    rx.box(
                        rx.link(
                            rx.button(
                                "보 기",
                                size="3",
                                style={
                                    "_hover": {
                                    "cursor": "pointer",
                                    "bg": rx.color("accent", 10),
                                    }
                                }
                                ),
                            #href=f"{MRAState.full_raw_path}{file["name"]}",
                            href=f"/workers/{MRAState.wonbu_no_var}/mra/{file["name"]}"
                            #href=file_url, #"http://localhost:8000/_upload/mra/1234/sample_4.pdf"
                            #is_external=True,
                            ),
                        #rx.button("보 기", size="2", width="80px"),
                        text_align="end",
                        width="15%"
                    ),
                    align="center",
                ),
                border="solid",
                border_color=rx.color("gray", 6),
                border_width="1px",
                border_radius="5px",
                padding ="0.7em",
                margin_top="1em",
                margin_left="0.1em",
                margin_right="0.1em",
            ),

def list_page() -> rx.Component:
    my_child = rx.box(
        #rx.image(src="http://localhost:8000/_upload/mra/1234/sample_4.pdf"),
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("의무기록지 파일 분석", size="4"),
            align="start",
            padding_bottom="1em",
        ),
        # contents
        rx.vstack(
            rx.text("아래 업로드 내역에서 파일을 선택하여 작업을 진행해 주세요 *", 
                    size="5",
                    font_family="NotoSansKR-Bold"),
            align="center",
            padding="2em",
        ),
        rx.vstack(
            file_upload_v1(),
            align="center",
            padding_bottom="1em",
            width="100%"
        ),
        rx.vstack(
            rx.box(
                rx.text("업로드 내역 (최근순)"),
                rx.cond(
                  MRAState.files.length() > 0,
                  rx.foreach(MRAState.files, file_item),
                  rx.vstack(
                      rx.text("현재 업로드된 파일이 없습니다. 파일을 업로드해 주세요.",
                              color=rx.color("gray", 9)),
                      rx.text("No files uploaded",
                              font_family="NotoSansKR-Bold",
                              color=rx.color("gray", 9)),
                      width="100%",
                      padding_y="10px",
                      align="center", #vstack에 속한 콘텐츠들 중앙 정렬
                      ),
                ),
                border="solid",
                border_color=rx.color("gray", 6),
                border_width="2px",
                border_radius="10px",
                width="800px", #75%
                #height="50vh",
                padding="1em",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px",
            ),
            align="center", # 큰 박스가 전체 페이지에서 센터
        ),
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)

