import reflex as rx
#
from .state import MRAState
from ..ui import dashboard_page
#
#
def detail_page() -> rx.Component:

    my_child = rx.box(
        # contents
        rx.hstack(
            rx.box(
                rx.el.Embed(
                    src=f"data:application/pdf;base64,{MRAState.base64_pdf}#view=FitV", # #toolbar=0
                    height="88vh",
                    width="100%",
                ),
                width="60%",
            ),
            rx.box(
                rx.text("색인 구역"),
                width="40%"
            ),
        ),
        padding_top="5em",
    )
    return dashboard_page(my_child)
