import reflex as rx
#
from .state import ATPAState
from ..ui import dashboard_page
#
#
def atpa_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("요양기간 분석자료 보기", size="3"),
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
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)

