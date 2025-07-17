import reflex as rx
import pandas as pd
import asyncio
#
from .utils.connections import ygtest_conn
from ..navigation import NavState
#
#
class MCFState(NavState):

    """ 
    원부번호가 입력되지 않을 시, 원부번호 추가
    """
    alert_button_loading_tf: bool = False
    @rx.event
    async def add_wonbu_no(self, form_data:dict):
        self.alert_button_loading_tf = True
        yield
        self.wonbu_no = form_data["wonbu_no"]
        
        #yield rx.redirect(f"{navigation.routes.HRA_ROUTE}?wonbu={self.wonbu_no}")
        yield self.to_mcf()
        self.alert_button_loading_tf = False




