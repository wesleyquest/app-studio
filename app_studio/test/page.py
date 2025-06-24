import reflex as rx
#
from ..ui.dashboard import dashboard_page
from .models import Summary
from .. import navigation
#
#
class TestState(rx.State):
    value = "tab1"
    @rx.event
    def change_value(self):
        if self.value == "tab2":
            self.value = "tab1"
        else:
            self.value = "tab2"    




def test_page() -> rx.Component:
    my_child = rx.box(
        rx.hstack(
            rx.icon("app-window", stroke_width="1.5", size=25),
            rx.text("TEST", size="4"),
            rx.text(">", size="4"),
            rx.text("건보수진내역 보기", size="4"),
            align="start",
            padding_bottom="1em",
        ),
        rx.center(
            rx.vstack(
                rx.box(
                rx.tabs.root(
                    rx.tabs.list(
                            rx.tabs.trigger(
                                rx.text("Tab 1"),
                                value="tab1",
                                width="50%"),

                        rx.tabs.trigger(
                            "Tab 2", 
                            value="tab2",
                            width="50%"),
                        size="2",
                    ),
                    rx.tabs.content(
                        rx.text("items on tab 1"),
                        rx.button("hi", on_click=TestState.change_value),
                        value="tab1",
                    ),
                    rx.tabs.content(
                        rx.text("items on tab 2"),
                        rx.button("hi", on_click=TestState.change_value),
                        value="tab2",
                    ),
                    value=TestState.value,
                ),
            width="100%"
            ),
                width="70%"
            )
        ),
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)
    


