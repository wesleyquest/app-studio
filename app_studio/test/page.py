import reflex as rx
from typing import List
#
from ..ui.dashboard import dashboard_page
from .models import Summary
from .. import navigation
#
#
class TestState(rx.State):   

    @rx.event
    def add_wonbu_no(self, form_data:dict):
        print(form_data)
        navigation.NavState.wonbu_no = form_data["wonbu_no"]
        print(navigation.NavState.wonbu_no)
        
        return rx.redirect(f"/hra?wonbu={navigation.NavState.wonbu_no}")


def insert_wonbu_dialog() -> rx.Component:
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access", color_scheme="red"),
    ),
    rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Add New User",
            ),
            rx.alert_dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="원부번호 입력", name="wonbu_no"
                    ),
                    rx.flex(
                        #rx.alert_dialog.cancel(
                        #    rx.button(
                        #        "Cancel",
                        #        variant="soft",
                        #        color_scheme="gray",
                        #    ),
                        #),
                        rx.alert_dialog.action(
                            rx.button(
                                "Submit", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=TestState.add_wonbu_no,
                reset_on_submit=False,
            ),
        style={"max_width": 450},
    ),
    open=rx.cond(
        navigation.NavState.wonbu_no != "none",
        False,
        True
    )
)


def test_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("layout-dashboard"),
            rx.text("앱 목록", size="4"),
            align="start",
            padding_bottom="2em",
        ),
        # contents
        insert_wonbu_dialog(),
        
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)
    


