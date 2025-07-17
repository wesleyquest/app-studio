import reflex as rx
#
from .state import MCFState
from ..components import insert_wonbu_dialog
from ..ui import dashboard_page
#
#
def mcf_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("재해조사서 검사표 요약 작성", size="3"),
            align="start",
            padding_left="0.5em",
            padding_bottom="1em",
        ),
        # contents
        rx.center(
            rx.hstack(
                rx.box(
                    rx.text("")
                ),
                width="100%"
            ),
            rx.box(
                insert_wonbu_dialog(MCFState),
                style={"display": "none"}
            )
            
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)

