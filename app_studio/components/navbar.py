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
                    rx.el.div(
                        "WQ",
                        class_name="text-white font-medium text-lg mr-1.5 p-1.5 bg-slate-800 rounded",
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
                    ),
                    rx.button("Log In", size="3"),
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
                    rx.el.div(
                        "WQ",
                        class_name="text-white font-medium text-lg mr-1 p-1 bg-slate-800 rounded",
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
        #bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        # top="0px",
        z_index="5",
        width="100%",
    )