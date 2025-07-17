import reflex as rx
#
from .state import HCRState
from ..ui import dashboard_page
from ..components import insert_wonbu_dialog
#
#
def hcr_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("app-window"),
            rx.text("건강검진 결과 요약", size="3"),
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
                insert_wonbu_dialog(HCRState),
                style={"display": "none"}
            )
            
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)

