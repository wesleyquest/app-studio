import reflex as rx
#
from ..ui import dashboard_page
#
#
def health_record_page() -> rx.Component:
    my_child = rx.vstack(
        rx.text("hello"),
        padding_top="5em",
    )
    return dashboard_page(my_child)