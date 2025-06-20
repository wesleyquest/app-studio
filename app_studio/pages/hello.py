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
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Open Dialog")),
                rx.dialog.content(
                    rx.dialog.title("Welcome to Reflex!"),
                    rx.dialog.description(
                        "This is a dialog component. You can render anything you want in here.",
                    ),
                    rx.dialog.close(
                        rx.button("Close Dialog", size="3"),
                    ),
                    rx.box(
                        rx.text("hello world"),
                        width="1800px",
                        height="900px",
                        border="gray",                       
                    ),
                    size="4"
                ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center"
        ),
    )
    return dashboard_page(my_child)
    