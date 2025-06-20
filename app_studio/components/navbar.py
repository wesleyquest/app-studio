import reflex as rx
#
from .. import navigation
#
#
def navbar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.color_mode_cond(
                light = rx.icon(icon, color="black"),
                dark = rx.icon(icon, color="white"),
            ),
            rx.color_mode_cond(
                light = rx.text(text, size="4", color="black"),
                dark = rx.text(text, size="4", color="white"),
            ),            
            
            width="100%",
            #padding_x="0.5rem",
            #padding_y="0.5rem",
            padding_x="10px",
            padding_y="10px",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        underline="none",
        weight="medium",
        width="100%",
        href=href,
    )

def navbar_items() -> rx.Component:
    return rx.vstack(
        navbar_item("앱 목록", "layout-dashboard", navigation.routes.HOME_ROUTE),
        navbar_item("RAG", "app-window", navigation.routes.RAG_ROUTE),
        navbar_item("의무기록지 파일 분석", "app-window", f"/workers/{navigation.NavState.wonbu_no_var}/mra"),
        navbar_item("건강보험 내역 분석", "app-window", f"/workers/{navigation.NavState.wonbu_no_var}/hra"),
        spacing="1",
        width="100%",
    )

def navbar_v1() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    # drawer
                    rx.drawer.root(
                        rx.drawer.trigger(
                            rx.icon(
                                "align-justify",
                                size=42,
                                style={
                                    "_hover": {
                                        "cursor": "pointer",
                                        "bg": rx.color("accent", 4),
                                        "color": rx.color("accent", 11),
                                    },
                                    "padding": "10px",
                                    "border-radius": "0.5em",
                                },
                            )
                        ),
                        rx.drawer.overlay(z_index="5"),
                        rx.drawer.portal(
                            rx.drawer.content(
                                rx.vstack(
                                    rx.hstack(
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
                                    #justify="end",
                                    width="100%",
                                    align_items="center",
                                    padding_bottom="10px",
                                    ),
                                    navbar_items(),
                                    #spacing="5",
                                    width="100%",
                                    align="center",
                                ),
                                top="auto",
                                right="auto",
                                height="100%",
                                #width="20em",
                                width="240px",
                                #padding="1.5em",
                                padding="15px",
                                bg=rx.color("accent", 1),
                            ),
                            width="100%",
                        ),
                        direction="left",
                    ),
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
                    width="100%",
                    #padding_x="0.5rem",
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
        # 공통
        bg=rx.color("accent", 1),
        border_bottom="1px solid #ccc",
        padding_y="10px",
        padding_x="19px",
        position="fixed",
        # top="0px",
        z_index="5",
        width="100%",
    )