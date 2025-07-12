import reflex as rx
#
from . import routes
#
#
class NavState(rx.State):
    wonbu_no: str = "none"
    
    @rx.event
    def set_wonbu_no(self):
        if self.router.page.params.get("wonbu", "none") != "none":
            self.wonbu_no = self.router.page.params.get("wonbu", "none")
        print(self.wonbu_no)

#    @rx.var
#    def wonbu_no_var(self) -> str:
        #print("MRAState wonbu_no var: ",  self.router.page.params.get("wonbu_no", "no data"))
#        print(self.router.page.params.get("wonbu", "none"))
#        if self.router.page.params.get("wonbu", "none") == "none":
#            return self.wonbu_no_var
#        return self.router.page.params.get("wonbu", "none")


    #wonbu_no_var: str = "none"
    #def set_wonbu_no_var(self):
    #    # wonbu_no_var 세팅 : wonbu_no_var가 ""(초기값)이고, url에 값이 주어진 경우
    #    if (self.wonbu_no_var == "none") & (self.router.page.params.get("wonbu_no", "none") != "none"):
    #        self.wonbu_no_var = self.router.page.params.get("wonbu_no", "none")
    #        print(f"set wonbu_no_var: {self.wonbu_no_var}")

    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_mra(self):
        return rx.redirect(f"/workers/{self.wonbu_no_var}/mra")
    def to_hra(self):
        return rx.redirect(f"/workers/{self.wonbu_no_var}/hra")




