import reflex as rx
#
from . import routes
#
#
"""
wonbu_no 가 저장된 메인 state
"""
class NavState(rx.State):
    wonbu_no: str = "none"
    alert_open_tf: bool = False

    @rx.event
    @rx.event
    def set_wonbu_no(self):
        if self.router.page.params.get("wonbu", "none") != "none":
            self.wonbu_no = self.router.page.params.get("wonbu", "none")
        print(self.wonbu_no)
        
    @rx.event
    async def open_alert_dialog(self):
        yield
        if self.wonbu_no == "none":
            self.alert_open_tf = True
        else:
            yield
            self.alert_open_tf = False
            yield

    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_hra(self):
        #return rx.redirect(f"/workers/{self.wonbu_no_var}/hra")
        return rx.redirect(f"{routes.HRA_ROUTE}?wonbu={self.wonbu_no}")
    def to_mra(self):
        #return rx.redirect(f"/workers/{self.wonbu_no_var}/mra")
        return rx.redirect(f"{routes.MRA_ROUTE}?wonbu={self.wonbu_no}")
    def to_mra_view(self, id):
        return rx.redirect(f"{routes.MRA_VIEW_ROUTE}?wonbu={self.wonbu_no}&id={id}")
    def to_hcr(self):
        return rx.redirect(f"{routes.HCR_ROUTE}?wonbu={self.wonbu_no}")
    def to_mcf(self):
        return rx.redirect(f"{routes.MCF_ROUTE}?wonbu={self.wonbu_no}")
    def to_tpa(self):
        return rx.redirect(f"{routes.TPA_ROUTE}?wonbu={self.wonbu_no}")
    def to_atpa(self):
        return rx.redirect(routes.ATPA_ROUTE)

