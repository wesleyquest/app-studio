import reflex as rx
from typing import List
#
from ..ui.dashboard import dashboard_page
from .models import Summary
from .. import navigation
#
#
APP_LIST=[
    {
        "no": 0, 
        "name": "건강보험 수진내역 추출 및 생성",
        "content": "재해자의 건강보험 내역에서 상병과 연관된 내역을 선택하고 재해조사서 생성",
        "category": "재해조사서",
        "tags": ["AI", "LLM"],
    },
    {
        "no": 1, 
        "name": "의무기록 파일 색인 및 요약",
        "content": "재해자의 의무기록에서 텍스트를 추출하고 상병과 연관된 내용을 색인 및 요약",
        "category": "재해조사서",
        "tags": ["OCR", "AI", "LLM"],
    },
    {
        "no": 2, 
        "name": "요양기간 분석",
        "content": "재해자의 요양기간에 대한 분석 정보 제공",
        "category": "요양기간",
        "tags": ["AI"],
    },
]

class AppDescription(rx.Model, table=False):
    no: int
    name: str
    content: str
    tags: List[str]


CATEGORY_LIST = ["전체", "재해조사서", "요양기간"]

class AppListState(rx.State):
    #apps: List[dict] = APP_LIST
    apps: List[AppDescription] = []
    category: str = "전체"
    
    @rx.event
    def change_category(self, selected: str) -> None:
        self.apps = []
        if selected != "전체":
            for app in APP_LIST:
                if app['category'] == selected:
                    self.apps.append(app)
        else:
            for app in APP_LIST:
                self.apps.append(AppDescription(**app))
        self.category = selected
        
    @rx.event
    def load_apps(self) -> None:
        self.category = "전체"
        #self.apps = APP_LIST
        for app in APP_LIST:
            self.apps.append(AppDescription(**app))


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
        rx.text(tag, size="3"),
        size="3"
    )

def app_component(app):
    return rx.box(
        rx.foreach(app.tags, tag_badge_component),
        rx.text(app["name"], font_family="NotoSansKR-Bold", size="3"),
        rx.text(app["content"]),
        background_color=rx.color("gray", 2),
        border_radius="10px",
        padding="1em",
        style={
        "_hover": {
            "cursor": "pointer",
            "bg": rx.color("accent", 4),
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
        rx.grid(
            rx.foreach(AppListState.apps, app_component),
            columns="5",
            spacing="3"
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
        rx.center(
            rx.hstack(
                rx.box(
                    app_list_component(),
                    width="100%",
                    min_height="80vh",
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
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)
    


