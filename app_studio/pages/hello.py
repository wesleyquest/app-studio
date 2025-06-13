import reflex as rx
#
from ..ui import dashboard_page
#
#
def index_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.container(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center"
        ),
    )
    return dashboard_page(my_child)
    