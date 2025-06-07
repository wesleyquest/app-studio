import reflex as rx
#
from . import routes
#
#
class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_ai_ocr(self):
        return rx.redirect(routes.MRA_ROUTE)




