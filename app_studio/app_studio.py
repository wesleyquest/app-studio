import reflex as rx
from rxconfig import config
#
from . import navigation
from .pages import index_page
from . import mra, hra, rag
from . import test
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
        "/styles/pdf_style.css",
    ],
    style = {"font_family": "NotoSansKR-Regular"}
)

app.add_page(index_page,
             route=navigation.routes.HOME_ROUTE,
             title="HOME")

app.add_page(
    mra.list_page,
    on_load=[ mra.MRAState.load_files],
    route=navigation.routes.MRA_ROUTE,
    title="MRA - LIST")

app.add_page(
    mra.detail_page,
    on_load=[ mra.MRAState.load_current_file],
    route=navigation.routes.MRA_DETAIL_ROUTE,
    title="MRA - DETAIL")

app.add_page(
    hra.hra_page,
    route=navigation.routes.HRA_ROUTE,
    title="HRA")

app.add_page(
    rag.rag_page,
    route=navigation.routes.RAG_ROUTE,
    title="RAG")

# test
app.add_page(
    test.test_page,
    #on_load=test.page.TestState.load_summaries,
    route="/test",
    title="TEST"
)



