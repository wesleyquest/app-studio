import reflex as rx
from reflex.components.component import NoSSRComponent
#
from .state import MRAState
from ..ui import dashboard_page
from ..navigation import NavState
from ..components import insert_wonbu_dialog
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

def summary_list_item(summary) -> rx.Component:
    """4: vstack - 페이지별 내용"""
    return rx.box(
            rx.text(f"{summary.page} 페이지", font_family="NotoSansKR-Bold",),
            rx.foreach(summary.content, summary_content_item),
            as_='button',
            on_click=MRAState.change_current_page(summary.page),
            border="solid",
            border_width="1px",
            border_color=rx.color("gray", 6),
            border_radius="8px",
            #box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px",
            padding_x="1em",
            padding_y="0.5em",
            width="100%",
            style={
            "_hover": {
                "cursor": "pointer",
                "bg": rx.color("accent", 4),
                "border_color": rx.color("accent", 8)
                #"color": rx.color("accent", 11),
                },
            },
            
        )

def pdf_item() -> rx.Component:
    return rx.box(
        pdf_view(
            file_info=[f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no}/{MRAState.mra_id}.pdf", MRAState.current_file_page]
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
                    file_info=[f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no}/{MRAState.mra_id}.pdf", page]
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
                        #rx.icon("square-pen", stroke_width="1.5", size=20),
                        rx.text("전체 문서 요약",
                                font_family="NotoSansKR-Bold"),
                        align="center"
                    ),
                    rx.text("이 문서는 2025년 하반기 신규 프로젝트 기획안으로, 총 5개 부문(마케팅, 개발, 디자인, 재무, 운영)에 걸친 종합 계획을 담고 있습니다. 주요 내용으로는 시장 분석 및 타겟 고객 정의, 핵심 기능 개발 로드맵, UI/UX 디자인 가이드라인, 예산 계획 및 수익 모델, 그리고 팀 구성 및 일정 관리 방안이 포함되어 있습니다. 특히 페이지 45-67에서는 핵심 기술 스택과 개발 방법론에 대한 상세 설명이, 페이지 78-92에서는 재무 계획 및 투자 수익률 분석이 중점적으로 다루어지고 있습니다."),
                    background_color="var(--gray-3)",
                    border_radius="10px",
                    padding="1em", # vstack '안'에 스페이싱 주기,
                    #margin_bottom="0.8em", # vstack '밖' 위아래에 스페이싱 주기
                    width="100%"
                ),
                # text
                rx.text("페이지별 주요 내용",
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


def summary_tab_component() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger(
                rx.text("파일 요약 정보", size="3", font_family="NotoSansKR-Bold"),
                value="tab1",
                width="50%"),
            rx.tabs.trigger(
                rx.text("재해자 상병 정보", size="3", font_family="NotoSansKR-Bold"), 
                value="tab2",
                width="50%"),
            size="2",
        ),
        rx.tabs.content(
            # 요약
            rx.box(
                rx.scroll_area(
                    summary_view(),
                    type="always",
                    scrollbars="vertical",
                    style={"height": "1000px"}, #"85vh", 960px
                ),
                #padding_x="1em",
                #width="50%",
                padding_top="1em",
                width="700px",
            ),
            value="tab1"
        ),
        rx.tabs.content(
            # 재해자 상병 정보
            rx.box(
                rx.hstack(
                    rx.text("재해자 상병 정보", font_family="NotoSansKR-Bold"), #
                    justify="center", #hstack 내부 콘텐츠 정렬
                    padding_bottom="1em",
                ),
                rx.scroll_area(
                    rx.flex(
                        rx.blockquote(
                            "Perfect typography is certainly the most elusive of all arts."
                        ),
                        rx.blockquote(
                            "Perfect typography is certainly the most elusive of all arts."
                        ),
                        rx.blockquote(
                            "Perfect typography is certainly the most elusive of all arts."
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    type="auto",
                    scrollbars="vertical",
                ),
                padding_top="1em",
                width="700px",
            ),
            value="tab2"
        ),
        default_value="tab1"
    )


def view_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("의무기록 파일 색인 및 요약 > 의무기록 파일 보기", size="3"),
            align="start",
            padding_left="0.5em",
            padding_bottom="1em",
        ),
        # 요약 및 pdf 뷰
        rx.center(
            rx.hstack(
                # pdf 뷰
                rx.box(
                    # pagination
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("arrow-left", size=20),
                                        rx.text("목록 돌아가기"),
                                    ),
                                    style={
                                        "_hover": {
                                            "cursor": "pointer",
                                        }
                                    },
                                    on_click=MRAState.to_mra(),
                                ),
                                text_align="start", # box contents horizontal 위치 align
                                width="50%",
                            ), 
                            rx.box(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("download", size=20),
                                        rx.text("파일 다운로드"),
                                    ),
                                    style={
                                        "_hover": {
                                            "cursor": "pointer",
                                        }
                                    },
                                    on_click=rx.redirect(
                                        f"{rx.get_upload_url("")}/mra/{MRAState.wonbu_no}/{MRAState.mra_id}.pdf",
                                        is_external=True,
                                    ),
                                ),
                                text_align="end", # box contents horizontal 위치 align
                                width="50%",
                            ),
                            width="800px"
                        ),

                        rx.hstack(
                            rx.button("이전", 
                                      variant="outline", 
                                      on_click=MRAState.prev_page,
                                      style={
                                      "_hover": {
                                          "cursor": "pointer",
                                          "bg": rx.color("accent", 4),
                                          "border_color": rx.color("accent", 8)
                                          },
                                      },
                                    ),
                            rx.text(
                                #f"Page {HRAState.page_number} / {HRAState.total_pages}"
                                f"{MRAState.current_file_page} 페이지 / 총 {MRAState.current_file_number_of_pages} 페이지"
                            ),
                            rx.button("다음", 
                                      variant="outline", 
                                      on_click=MRAState.next_page,
                                      style={
                                      "_hover": {
                                          "cursor": "pointer",
                                          "bg": rx.color("accent", 4),
                                          "border_color": rx.color("accent", 8)
                                          },
                                      },                                      
                                      ),
                            align="center",
                        ),
                        align="center",
                        padding_bottom="1em",  
                    ),
                    # pdf
                    rx.vstack(
                        rx.box(
                            rx.center(
                                pdf_item(),
                            ),
                            #border="solid",
                            #border_color=rx.color("gray", 6),
                            #border_width="1px",
                            #border_radius="5px",
                            #padding_x="1em",
                            #width="50%",
                            width="800px",
                            #height="85vh",
                            height="980px"  
                        ),                    
                    ),
                    min_height="1100px", #"150vh",
                    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    background_color=rx.color("accent", 1),
                    border_radius="10px",
                    padding="1em", #박스 안
                    margin_x="2em",
                ),
                # 요약
                rx.box(
                    summary_tab_component(),
                    #max_width="400px",
                    #min_width="300px",
                    min_height="1100px", #"150vh",
                    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    background_color=rx.color("accent", 1),
                    border_radius="10px",
                    padding="1em", #박스 안
                    margin_x="2em",
                ),
                width="100%"
            ),
        ),
        insert_wonbu_dialog(MRAState),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)

