import reflex as rx
#
from .state import HRAState
from ..components import insert_wonbu_dialog
from ..ui import dashboard_page
from ..navigation import NavState
#
#
"""
데이터가 많지 않기 때문에 한번에 state에 로드
in-memory filtering and sorting 방식
"""

def table_column(column_name: str):
    return rx.table.column_header_cell(
        rx.text(column_name,
                size="3",
                font_family="NotoSansKR-Bold",
                )
    )

def table_row(data: dict[str, str], columns: list[str], index: int):
    return rx.table.row(
                rx.table.cell(
                    rx.checkbox(
                        checked=rx.cond(
                            #HRAState.selected_rows.contains(index), True, False
                            HRAState.selected_rows.contains(data['no']), True, False
                        ),
                        # row 자체 클릭도 적용되어 있어서, 클릭 시 두번 클릭되어 주석 처리
                        #on_change=lambda: HRAState.toggle_row_selection(index),
                        size="3",
                        cursor="pointer",
                    )
                ),
                rx.foreach(
                    columns,
                    lambda column: rx.table.cell(rx.text(data[column])),
                ),
                background=rx.cond(
                    #HRAState.selected_rows.contains(index), rx.color("indigo", 3), "none"
                    HRAState.selected_rows.contains(data['no']), rx.color("indigo", 3), "none"
                ),
                _hover={"bg": rx.color("indigo", 3)},
                white_space="nowrap",
                align="center",
                cursor="pointer",
                on_click=lambda: HRAState.toggle_row_selection(index)
            )

def hra_table(
    data: list[dict] | rx.Var[list[dict]],
    columns: list[str] | rx.Var[list[str]],
    header_columns: list[str] | rx.Var[list[str]],
):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell(
                    rx.text(""),
                    # 전체 선택 제외
                    #rx.checkbox(
                    #    checked=rx.cond(
                    #        HRAState.selected_rows.length() == data.length(), True, False
                    #    ),
                    #    on_change=lambda: HRAState.toggle_select_all(),
                    #    size="3",
                    #    cursor="pointer",
                    #),
                ),
                rx.foreach(header_columns, table_column),
                white_space="nowrap",
            ),
        ),
        rx.table.body(
            rx.foreach(
                data,
                lambda data_set, index: table_row(data_set, columns, index),
            ),
        ),
        width="100%",
        max_width="1400px",
        variant="surface",
        #size="1",
    )
    
def result_skeleton() -> rx.Component:
    return rx.vstack(
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
        rx.skeleton(
            rx.text("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ"),
        ),
    )
    
def hra_profile_component() -> rx.Component:
    return rx.fragment(
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
    )
    
def hra_main_component() -> rx.Component:
    return rx.vstack(
                rx.box(
                rx.vstack(
                    rx.text("1. 건강보험 수진내역에서 재해자의 상병과 연관된 내역을 선택해 주세요. (AI가 연관된 내역을 미리 선택했어요.)", size="3", font_family="NotoSansKR-Bold"),
                    #padding_bottom="1em",
                ),
                rx.hstack(
                    rx.cond(
                        HRAState.tab_value == "tab1",
                        rx.button("재해조사서 초안 생성", size="3", on_click=HRAState.generate_summary),
                        rx.button("내역으로 돌아가기", size="3", on_click=HRAState.reset_summary),
                    ),
                    justify="end",
                ),
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger(
                            rx.text("건강보험 수진내역 선택", size="3", font_family="NotoSansKR-Bold"),
                            value="tab1",
                            width="50%"),
                        rx.tabs.trigger(
                            rx.text("재해조사서 초안 생성", size="3", font_family="NotoSansKR-Bold"), 
                            value="tab2",
                            width="50%"),
                        size="2",
                    ),
                    rx.tabs.content(
                        rx.vstack(
                            rx.hstack(
                                rx.button("이전", variant="outline", on_click=HRAState.prev_page),
                                rx.text(
                                    #f"Page {HRAState.page_number} / {HRAState.total_pages}"
                                    f"{HRAState.page_number} 페이지 / 총 {HRAState.total_pages} 페이지"
                                ),
                                rx.button("다음", variant="outline", on_click=HRAState.next_page),
                                align="center",
                            ),
                            align="center",
                            padding_top="1em",
                            padding_bottom="1em",  
                        ),
                        rx.vstack(
                            hra_table(HRAState.paginated_data, HRAState.columns, HRAState.header_columns),
                            #class_name="w-full h-full flex flex-col items-center justify-center",
                            align="center",
                        ),
                        value="tab1",
                    ),
                    rx.tabs.content(
                        #rx.hstack(
                        #    rx.button("내역으로 돌아가기", size="3", on_click=HRAState.reset_summary),
                        #    justify="end",
                        #    padding_top="1em",
                        #),
                        rx.vstack(
                            rx.cond(
                                HRAState.summary == "",
                                result_skeleton(),
                                rx.text(HRAState.summary),
                            ),
                            margin_top="1em", #vstack 외부
                            padding="1em", #vstack 내부
                            border="solid",
                            border_width="1px",
                            border_color=rx.color("gray", 6),
                            border_radius="4px",
                        ),
                        value="tab2",
                    ),
                    value=HRAState.tab_value,
                ),
                width="100%",
            ),
            width="100%",
            #padding_top="2em",
            )
"""
def insert_wonbu_dialog() -> rx.Component:
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access", color_scheme="red"),
    ),
    rx.alert_dialog.content(
            rx.alert_dialog.title(
                "원부번호 입력",
            ),
            rx.alert_dialog.description(
                "재해자의 원부번호를 입력하세요.",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="원부번호", name="wonbu_no"
                    ),
                    rx.flex(
                        #rx.alert_dialog.cancel(
                        #    rx.button(
                        #        "Cancel",
                        #        variant="soft",
                        #        color_scheme="gray",
                        #    ),
                        #),
                        rx.alert_dialog.action(
                            rx.button(
                                "적용", type="submit", loading=HRAState.alert_button_loading_tf
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=HRAState.add_wonbu_no,
                reset_on_submit=False,
            ),
        style={"max_width": 450},
    ),
    open=HRAState.alert_open_tf
)
"""  

def hra_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("건강보험 내역 추출 요약", size="3"),
            align="start",
            padding_left="0.5em",
            padding_bottom="1em",
        ),
        # contents
        rx.center(
            rx.hstack(
                rx.box(
                    hra_profile_component(),
                    width="20%",
                    max_width="400px",
                    min_width="300px",
                    min_height="84vh",
                    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    background_color=rx.color("accent", 1),
                    border_radius="10px",
                    padding="1em", #박스 안
                    margin_x="1em",
                ),
                rx.box(
                    hra_main_component(),
                    width="80%",
                    max_width="1400px",
                    min_height="84vh",
                    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    background_color=rx.color("accent", 1),
                    border_radius="10px",
                    padding="1em",
                    margin_x="1em",
                ),
                width="100%"
            ),
            rx.box(
                insert_wonbu_dialog(HRAState),
                style={"display": "none"}
            )
            
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)





