import reflex as rx
#
#
def insert_wonbu_dialog(state) -> rx.Component:
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access", color_scheme="red"),
    ),
    rx.alert_dialog.content(
            rx.alert_dialog.title(
                "원부번호 입력",
            ),
            rx.alert_dialog.description(
                "재해자의 원부번호를 입력하세요.",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="원부번호", name="wonbu_no"
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
                                "적용", type="submit", loading=state.alert_button_loading_tf
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=state.add_wonbu_no,
                reset_on_submit=False,
            ),
        style={"max_width": 450},
    ),
    open=state.alert_open_tf
)


    
