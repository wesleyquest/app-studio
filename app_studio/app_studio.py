import reflex as rx
from rxconfig import config
#
from . import navigation
from . import app_list
from . import mra, hra, hcr, mcf, tpa, atpa
from . import rag
from . import test
#
#
app = rx.App(
    theme=rx.theme(
        #appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="100%",
        radius="medium",
        accent_color="indigo"
    ),
    stylesheets=[
        "/fonts/myfont.css",
        "/styles/pdf_style.css",
    ],
    style = {"font_family": "NotoSansKR-Regular"}
)

app.add_page(
    app_list.app_list_page,
    on_load=[navigation.NavState.set_wonbu_no, app_list.AppListState.load_apps],
    route=navigation.routes.HOME_ROUTE,
    title="HOME")

app.add_page(
    hra.hra_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog, hra.HRAState.load_data],
    route=navigation.routes.HRA_ROUTE,
    title="HRA")

app.add_page(
    mra.list_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog, mra.MRAState.load_files],
    route=navigation.routes.MRA_ROUTE,
    title="MRA - LIST")

app.add_page(
    mra.view_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog, mra.MRAState.load_current_file],
    route=navigation.routes.MRA_VIEW_ROUTE,
    title="MRA - VIEW")

app.add_page(
    hcr.hcr_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog],
    route=navigation.routes.HCR_ROUTE,
    title="HCR")

app.add_page(
    mcf.mcf_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog],
    route=navigation.routes.MCF_ROUTE,
    title="MCF")

app.add_page(
    tpa.tpa_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog],
    route=navigation.routes.TPA_ROUTE,
    title="TPA")

app.add_page(
    atpa.atpa_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog],
    route=navigation.routes.ATPA_ROUTE,
    title="ATPA")


""" 
app.add_page(
    mra.list_page,
    on_load=[mra.MRAState.load_files],
    route=navigation.routes.MRA_ROUTE,
    title="MRA - LIST")

app.add_page(
    mra.detail_page,
    on_load=[mra.MRAState.load_current_file],
    route="/asdf",
    title="MRA - DETAIL")

app.add_page(
    mra.mra_page,
    on_load=[navigation.NavState.set_wonbu_no, navigation.NavState.open_alert_dialog, mra.MRAState.load_current_file],
    route=navigation.routes.MRA_ROUTE,
    title="MRA")
"""

app.add_page(
    rag.rag_page,
    route=navigation.routes.RAG_ROUTE,
    title="RAG")

# test
app.add_page(
    test.test_page,
    #on_load=test.page.AppListState.load_apps,
    route="/test",
    title="TEST"
)



