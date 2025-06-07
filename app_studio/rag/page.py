import reflex as rx
#
from ..ui import dashboard_page
#
#
def rag_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.container(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("This is rag page.", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center"
        ),
    )
    return dashboard_page(my_child)