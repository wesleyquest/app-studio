import reflex as rx
#
from ..ui.dashboard import dashboard_page
from .models import CATEGORY_LIST
from .state import AppListState
#
#
def badge_component(category) -> rx.Component:
    return  rx.cond(
        category == AppListState.category,
        rx.box(
            rx.badge(rx.text(category, font_family="NotoSansKR-Bold", size="3"), 
                        radius="full", size="3", variant="solid",
                        style={
                        "_hover": {
                            "cursor": "pointer",
                            "bg": rx.color("accent", 4),
                            "color": rx.color("accent", 11),
                            },
                        },
                    ),
            as_='button',
            on_click=AppListState.change_category(category),
        ),
        rx.box(
            rx.badge(rx.text(category, font_family="NotoSansKR-Bold", size="3"), 
                        radius="full", size="3", variant="outline",
                        style={
                        "_hover": {
                            "cursor": "pointer",
                            "bg": rx.color("accent", 4),
                            "color": rx.color("accent", 11),
                            },
                        },
                    ),
            as_='button',
            on_click=AppListState.change_category(category),
        ),
    )

def tag_badge_component(tag) -> rx.Component:
    return rx.badge(
        rx.text(tag),
        size="3",
        margin_right="0.5em",
    )

def app_component(app):
    return rx.box(
        rx.foreach(app.tags, tag_badge_component),
        rx.text(app["name"], font_family="NotoSansKR-Bold", size="3", padding_top="0.5em"),
        rx.text(app["content"]),
        width="300px",
        border="solid",
        border_width="1px",
        border_color=rx.color("gray", 6),
        #background_color=rx.color("gray", 2),
        border_radius="10px",
        padding="1em",
        style={
        "_hover": {
            "cursor": "pointer",
            "bg": rx.color("accent", 4),
            "border_color": rx.color("accent", 8)
            #"color": rx.color("accent", 11),
            },
        },
    )


def app_list_component() -> rx.Component:
    return rx.fragment(
        rx.hstack(
            rx.text("앱 목록", font_family="NotoSansKR-Bold", size="4"),
            justify="start", #hstack 내부 콘텐츠 정렬
            padding_bottom="1em",
        ),
        rx.flex(
            rx.foreach(CATEGORY_LIST, badge_component),
            spacing="3",
            padding_bottom="1em",
        ),
        rx.flex(
            rx.foreach(AppListState.apps, app_component),
            #columns="5",
            spacing="3",
            flex_wrap="wrap", # 창에 맞춰 밑으로 떨어지는 뷰
        )
    )

def app_list_page() -> rx.Component:
    my_child = rx.box(
        # navigation
        rx.hstack(
            rx.icon("layout-dashboard"),
            rx.text("앱 목록", size="4"),
            align="start",
            padding_left="0.5em",
            padding_bottom="1em",
        ),
        # contents
        rx.center(
            rx.hstack(
                rx.box(
                    app_list_component(),
                    width="100%",
                    min_height="84vh",
                    #box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
                    background_color=rx.color("accent", 1),
                    border_radius="10px",
                    padding_y="1em",
                    padding_x="1em",
                    margin_x="1em",
                ),
                width="100%"
            ),
        ),
        padding_top="4em",
        padding_left="4em",
    )
    return dashboard_page(my_child)