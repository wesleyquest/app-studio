import reflex as rx
from reflex.style import toggle_color_mode
#
from .. import navigation
#
#
def sidebar_item(
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
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("홈", "house", navigation.routes.HOME_ROUTE),
        sidebar_item("의무기록 분석", "dock", navigation.routes.MRA_ROUTE),
        sidebar_item("건강기록 분석", "dock", navigation.routes.HRA_ROUTE),
        sidebar_item("RAG", "dock", navigation.routes.RAG_ROUTE),
        spacing="1",
        width="100%",
    )

def sidebar_dark_mode_toggle_item() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.color_mode_cond(
                light=rx.icon("moon"),
                dark=rx.icon("sun"),
            ),
            rx.text(
                rx.color_mode_cond(
                    light="다크 모드로 변경",
                    dark="라이트 모드로 변경",
                ),
            ),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "cursor": "pointer",
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "color": rx.color("accent", 11),
                "border-radius": "0.5em",
            },
        ),
        on_click=toggle_color_mode,
        as_='button', # <button></button>
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_v1() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.scroll_area(
            rx.vstack(
                # rx.hstack(
                #     # rx.image(
                #     #     src="/logo.jpg",
                #     #     width="2.25em",
                #     #     height="auto",
                #     #     border_radius="25%", bg-gray-600
                #     # ),
                #     rx.el.div(
                #         "WQ",
                #         class_name="text-white font-medium text-lg mr-1.5 p-1.5 bg-slate-800 rounded",
                #     ),
                #     rx.heading(
                #         "App Studio", size="6", font_weight="bold"
                #     ),
                #     align="center",
                #     justify="start",
                #     padding_x="0.5rem",
                #     width="100%",
                # ),
                sidebar_items(),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="5em",
                bg=rx.color("accent", 1),
                align="start",
                # height="100%",
                height="100vh",
                width="16em",
            ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 1),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
            padding_top="5em",
        ),
    )

