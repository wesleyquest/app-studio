import reflex as rx
from typing import List
#
from .models import AppDescription, APP_LIST
from .. import navigation
#
#
class AppListState(navigation.NavState):
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
        self.apps = []
        self.category = "전체"
        #self.apps = APP_LIST
        for app in APP_LIST:
            self.apps.append(AppDescription(**app))
            
    @rx.event
    def go_page(self, app_name):
        #건강보험, 의무기록, 요양기간의 경우, url query parameter에 wonbu 추가
        if app_name == "건강보험 내역 추출 요약":
            #return rx.redirect(f"{navigation.routes.HRA_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_hra()
        if app_name == "의무기록 파일 보기":
            #return rx.redirect(f"{navigation.routes.MRA_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_mra()
        if app_name == "건강검진 결과 요약":
            #return rx.redirect(f"{navigation.routes.HCR_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_hcr()
        if app_name == "재해조사서 검사표 요약 작성":
            #return rx.redirect(f"{navigation.routes.MCF_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_mcf()      
        if app_name == "재해자 요양기간 분석":
            #return rx.redirect(f"{navigation.routes.TPA_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_tpa()
        else: #요양기간 분석자료 보기
            #return rx.redirect(f"{navigation.routes.ATPA_ROUTE}?wonbu={self.wonbu_no}")
            return self.to_atpa()

