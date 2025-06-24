import reflex as rx
#
from ..components import sidebar_v1, navbar_v1

def dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        rx.vstack(
            #rx.color_mode.button(position="bottom-left"),
            navbar_v1(),
            rx.hstack(
                # rx.theme_panel(default_open=True),
                sidebar_v1(),
                rx.box(
                    child,
                    padding="1em",
                    width="100%",
                    id="my-content-box",
                ),
                width="100%",
            ),
        ),

        # rx.color_mode.button(position="bottom-left"),
    )