import reflex as rx
#
from .state import TPAState
from ..components import insert_wonbu_dialog
from ..ui import dashboard_page
#
#
def tpa_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("재해자 요양기간 분석", size="3"),
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
                insert_wonbu_dialog(TPAState),
                style={"display": "none"}
            )
            
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)

