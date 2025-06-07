import reflex as rx
from rxconfig import config
#
from . import navigation
from .pages import index_page
from . import mra, hra, rag
#
#
app = rx.App(
    theme=rx.theme(
        #appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="indigo"
    ),
    stylesheets=[
        "/fonts/myfont.css",
    ],
    style = {"font_family": "NotoSansKR-Medium"}
)

app.add_page(index_page,
             route=navigation.routes.HOME_ROUTE,
             title="HOME")

app.add_page(
    mra.medical_record_page,
    route=navigation.routes.MRA_ROUTE,
    title="MRA")

app.add_page(
    hra.health_record_page,
    route=navigation.routes.HRA_ROUTE,
    title="HRA")

app.add_page(
    rag.rag_page,
    route=navigation.routes.RAG_ROUTE,
    title="RAG")

