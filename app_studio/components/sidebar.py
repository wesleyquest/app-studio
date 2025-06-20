import reflex as rx
from reflex.style import toggle_color_mode
#
from .. import navigation
#
#
def sidebar_item(
    text:str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.color_mode_cond(
                light = rx.icon(icon, color="black"),
                dark = rx.icon(icon, color="white"),
            ),
            rx.color_mode_cond(
                light = rx.text(text, size="1", color="black"),
                dark = rx.text(text, size="1", color="white"),
            ),   
            width="100%",
            #padding_x="1.5rem",
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

def sidebar_items() -> rx.Component:
    return rx.center(
        rx.vstack(
        sidebar_item("앱 목록", "layout-dashboard", navigation.routes.HOME_ROUTE),
        sidebar_item("앱 1", "app-window", navigation.routes.RAG_ROUTE),
        sidebar_item("앱 2", "app-window", f"/workers/{navigation.NavState.wonbu_no_var}/mra"),
        sidebar_item("앱 3", "app-window", f"/workers/{navigation.NavState.wonbu_no_var}/hra"),
        #spacing="1",
        width="100%",
    )
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
            rx.vstack(
                sidebar_items(),
                #spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                #padding_x="1em",
                #padding_y="5em",
                padding_y="70px",
                bg=rx.color("accent", 1),
                align="center",
                # height="100%",
                height="100vh",
                #width="100%",
                width="82px"
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
                            
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
            padding_top="5em",
        ),
    )


