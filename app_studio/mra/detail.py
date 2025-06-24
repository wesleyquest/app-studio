import reflex as rx
from reflex.components.component import NoSSRComponent
#
from .state import MRAState
from ..ui import dashboard_page
from .. import navigation
#
#
# Component
pdf_view_path = rx.asset("pdf_view.js", shared=True)
public_pdf_view_path = "$/public/" + pdf_view_path
class PdfView(NoSSRComponent): #NoSSRComponent
    # Use an absolute path starting with $/public
    library = public_pdf_view_path

    # Define everything else as normal.
    tag = "PdfView"
    
    # Props
    file_info: rx.Var[list] # 0: file_path, 1: page
    
pdf_view = PdfView.create

# Page
def summary_content_item(content):
    #return rx.text(content, size="4")
    return rx.list.item(content)

"""
def summary_list_item(summary) -> rx.Component:
    return  rx.vstack(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                page_view_button_dialog(summary.page),
                                rx.tooltip(
                                    rx.text(summary.type,
                                            padding_x="5px",
                                            padding_y="1px",
                                            font_family="NotoSansKR-Bold",
                                            color=rx.color("gray", 9),
                                            #border="solid",
                                            #border_width="1px",
                                            #border_color=rx.color("gray", 9),
                                            #border_radius="8px"
                                    ),
                                    content="This is the tooltip content."  
                                ),
                                align="center"
                            ),
                            width="50%"
                        ),
                        rx.box(
                            rx.hstack(
                            page_view_icon_dialog(summary.page),
                            rx.button(
                                rx.icon("square-arrow-out-up-right",
                                        color = "var(--indigo-11)"),
                                padding="0.5em",
                                height="2em",
                                background_color="transparent",
                                style={
                                    "_hover": {
                                        "cursor": "pointer",
                                        "bg": rx.color("accent", 4),
                                        #"color": rx.color("accent", 11),
                                    },
                                    #"color": rx.color("accent", 11),
                                    "border-radius": "0.5em",
                                },
                                on_click=rx.redirect(
                                    f"{rx.get_upload_url("")}/sample/샘플_1.pdf#page={summary['page']}",
                                    is_external=True,
                                    )
                            ), 
                            justify="end"                                
                            ),
                            width="50%",
                            text_align="end"
                        ),
                        width="100%",
                        #align="center" #hstack 안에 있는 컨텐츠의 수평 정렬
                    ),
                    #rx.text(f"{summary.content}",
                    #        size="4"),
                    rx.foreach(summary.content, summary_content_item),
                    width="100%"
                    #padding_left="1em", #vstack 왼쪽 여백                   
                ),
            border_radius="10px",
            border="1px solid #ccc",
            padding="1em", # vstack '안'에 스페이싱 주기,
            #margin_y="0.8em", # vstack '밖' 위아래에 스페이싱 주기
            #box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px",
            align="center",
            width="100%"
        )
"""
def summary_list_item(summary) -> rx.Component:
    """4: vstack - 페이지별 내용"""
    return rx.box(
            rx.text(f"{summary.page} 페이지", size="4", font_family="NotoSansKR-Bold",),
            rx.foreach(summary.content, summary_content_item),
            as_='button',
            on_click=MRAState.change_current_page(summary.page),
            border="solid",
            border_width="1px",
            border_color=rx.color("gray", 6),
            border_radius="8px",
            box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px",
            padding_x="1em",
            padding_y="0.5em",
            width="100%",
            style={
                "_hover": {
                    "cursor": "pointer",
                    "bg": rx.color("gray", 3),
                    #"color": rx.color("accent", 11),
                },
            },
            
        )

""" 
rx.card(
        rx.button(
            rx.text(summary.page),
            rx.foreach(summary.content, summary_content_item),
        ),
        as_child=True,
        width="100%"
    )
"""


def pdf_item() -> rx.Component:
    return rx.box(
        pdf_view(
            file_info=[f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no_var}/{MRAState.mra_id_var}.pdf", MRAState.current_file_page]
        ),
        #border="solid",
        #border_width="1px",
        #border_color="gray",
        #border_radius="10px",
        #padding_y="1em",
        #margin_top="1em",
    ) 




def dialog_content(page) -> rx.Component:
    return  rx.box(
                pdf_view(
                    file_info=[f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no_var}/{MRAState.mra_id_var}.pdf", page]
                ),
                border="solid",
                border_width="1px",
                border_color=rx.color("gray", 6),
                border_radius="10px",
                padding_y="1em",
                margin_top="1em",
            ) 


def page_view_button_dialog(page) -> rx.Component:
    return  rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.hstack(
                    rx.icon("file-text", stroke_width="1.5", size=20),
                    rx.text(f"{page} 페이지",
                            size="3"),
                    align="center"
                ),
                    size="4",
                    font_family="NotoSansKR-Bold",
                    padding="0.5em",
                    height="2em",
                    border="none",
                    background=rx.color("accent", 4),
                    color=rx.color_mode_cond(light="black", dark="white"),
                    style={
                        "_hover": {
                            "cursor": "pointer",
                            "bg": rx.color("accent", 6),
                        },
                    },
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                rx.text("자료 보기", font_family="NotoSansKR-Bold")
            ),
            rx.center(
                dialog_content(page)  
            ),
            max_width="800px",
            height="800px",
        ),
    ),

def page_view_icon_dialog(page) -> rx.Component:
    return  rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("picture-in-picture",
                        color = "var(--indigo-11)"),
                padding="0.5em",
                height="2em",
                background_color="transparent",
                style={
                    "_hover": {
                        "cursor": "pointer",
                        "bg": rx.color("accent", 4),
                        #"color": rx.color("accent", 11),
                    },
                    #"color": rx.color("accent", 11),
                    "border-radius": "0.5em",
                },
            )
        ),
        rx.dialog.content(
            rx.dialog.title(
                rx.text("자료 보기", font_family="NotoSansKR-Bold")
            ),
            rx.center(
                dialog_content(page)  
            ),
            max_width="800px",
            height="800px",
        ),
    ),


def summary_view() -> rx.Component:
    return  rx.center(
            rx.vstack(
                # 1: hstack - 파일 정보, 다운로드 버튼
                rx.hstack(
                    rx.box(
                        rx.text(MRAState.current_file_fullname,
                                size="6",
                                font_family="NotoSansKR-Bold",
                                ),
                        rx.hstack(
                            rx.icon("file-text", color="gray", stroke_width="1.5", size=20),
                            rx.text(f"총 {MRAState.current_file_number_of_pages} 페이지", size="3", color_scheme="gray"),
                            rx.icon("calendar-check", color="gray", stroke_width="1.5", size=20),
                            rx.text(f"업로드 일자: \u00A0 {MRAState.current_file_datetime}", size="3", color_scheme="gray"),
                            rx.icon("folder-check", color="gray", stroke_width="1.5", size=20),
                            rx.text(f"파일 사이즈: \u00A0 {MRAState.current_file_size}", size="3", color_scheme="gray"),
                            padding_top="1em", # 현재 hstack의 위 스페이싱
                            align="center" # hstack 안에 contents horizontal center
                        ),
                        #rx.text("총 124 페이지 | 업로드 날짜: 2025-06-18 | 파일 사이즈: 8.2MB",
                        #        size="4",
                        #        color_scheme="gray"),
                        width="100%"
                    ),
                    width="100%",
                    #align="center", # 한 라인에 있는 컨텐츠의 중심을 일치
                ),
                # 2: vstack - 전체 문서 요약
                rx.vstack(
                    rx.hstack(
                        rx.icon("square-pen", stroke_width="1.5", size=20),
                        rx.text("전체 문서 요약",
                                size="4",
                                font_family="NotoSansKR-Bold"),
                        align="center"
                    ),
                    rx.text("이 문서는 2025년 하반기 신규 프로젝트 기획안으로, 총 5개 부문(마케팅, 개발, 디자인, 재무, 운영)에 걸친 종합 계획을 담고 있습니다. 주요 내용으로는 시장 분석 및 타겟 고객 정의, 핵심 기능 개발 로드맵, UI/UX 디자인 가이드라인, 예산 계획 및 수익 모델, 그리고 팀 구성 및 일정 관리 방안이 포함되어 있습니다. 특히 페이지 45-67에서는 핵심 기술 스택과 개발 방법론에 대한 상세 설명이, 페이지 78-92에서는 재무 계획 및 투자 수익률 분석이 중점적으로 다루어지고 있습니다.",
                            size="4"),
                    background_color="var(--gray-3)",
                    border_radius="10px",
                    padding="1em", # vstack '안'에 스페이싱 주기,
                    #margin_bottom="0.8em", # vstack '밖' 위아래에 스페이싱 주기
                    width="100%"
                ),
                # text
                rx.text("페이지별 주요 내용",
                        size="4",
                        font_family="NotoSansKR-Bold",
                        padding_top="1em", # 위쪽 추가 스페이싱
                        ), 
                rx.foreach(MRAState.summaries, summary_list_item),
                width="100%",
                padding_x="1em",
                padding_y="1em",
                #justify="center",
                #align="center" # vstack 안에 contents horizontal center
            ),
            #center에는 파라미터 주지 말 것!
        ),


def detail_page() -> rx.Component:
    my_child = rx.box(
        # 네비게이션
        rx.hstack(
            rx.icon("app-window", stroke_width="1.5", size=25),
            rx.text("의무기록지 분석", size="4"),
            align="start",
            padding_bottom="1em",
        ),
        # 상단 메뉴
        rx.center(
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.icon("arrow-left-from-line", stroke_width="1.5", size=25),
                        rx.text("요약 보기", font_family="NotoSansKR-Bold"),
                    ),
                    width="700px",
                    text_align="center",
                ),
                rx.box(
                    rx.hstack(
                            rx.icon("arrow-left-from-line", stroke_width="1.5", size=25),
                            rx.text("파일 보기", font_family="NotoSansKR-Bold"),
                    ),
                    width="800px",
                    text_align="center",
                ),
                width="90%",
                #padding_x="2.25em", #1.5+0.75
                #padding_top="1em",
                padding_bottom="1em",
            ),
        ),
        # 요약 및 pdf 뷰
        rx.center(
            rx.hstack(
                # 요약
                rx.box(
                    rx.scroll_area(
                        summary_view(),
                        type="always",
                        scrollbars="vertical",
                        style={"height": "960px"}, #"85vh"
                    ),
                    padding_x="1em",
                    #width="50%",
                    width="700px",
                ),
                # pdf 뷰
                rx.vstack(
                    rx.box(
                        rx.button(
                            rx.hstack(
                                rx.icon("download"),
                                rx.text("파일 다운로드"),
                            ),
                            size="3",
                            style={
                                "_hover": {
                                    "cursor": "pointer",
                                }
                            },
                            on_click=rx.redirect(
                            f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no_var}/{MRAState.mra_id_var}.pdf",
                            is_external=True,
                            ),
                        ),
                        text_align="end", # box contents horizontal 위치 align
                        width="800px",
                    ),
                    rx.box(
                        rx.center(
                            pdf_item(),
                        ),
                        border="0.75em solid #ccc",
                        border_radius="8px",
                        padding_x="1em",
                        #width="50%",
                        width="800px",
                        #height="85vh",
                        height="960px"  
                    ),                    
                ),
                width="90%"
            ),
        ),
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)

