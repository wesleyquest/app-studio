import reflex as rx
from typing import List
#
from .models import AppDescription, APP_LIST
#
#
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
        self.apps = []
        self.category = "전체"
        #self.apps = APP_LIST
        for app in APP_LIST:
            self.apps.append(AppDescription(**app))