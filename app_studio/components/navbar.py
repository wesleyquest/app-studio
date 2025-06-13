import reflex as rx
#
#
def navbar_v1() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    # rx.image(
                    #     src="/logo.jpg",
                    #     width="2.25em",
                    #     height="auto",
                    #     border_radius="25%", bg-gray-600
                    # ),
                    rx.text(
                        "WQ",
                        size="4",
                        style={
                            "color": "white",
                            "background_color": "#646464",
                            "padding": "6px",
                            "border_radius": "5px"
                        }
                    ),
                    rx.heading(
                        "App Studio", size="5", font_weight="bold"
                    ),
                    align="center",
                    # justify="start",
                    # padding_x="0.5rem",
                    # width="100%",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                    ),
                    rx.button("Log In", size="3", color_scheme="gray"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.text(
                        "WQ",
                        size="3",
                        style={
                            "color": "white",
                            "background_color": "#646464",
                            "padding": "5px",
                            "border_radius": "4px"
                        }
                    ),
                    rx.heading(
                        "App Studio", size="5", font_weight="bold"
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="2",
                        variant="outline",
                    ),
                    rx.button("Log In", size="2"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 1),
        padding="1em",
        position="fixed",
        # top="0px",
        z_index="5",
        width="100%",
    )