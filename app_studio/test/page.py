import reflex as rx
from typing import List
import base64
#
from ..ui.dashboard import dashboard_page
#
#
class TestState(rx.State):
    base64_pdf: str = ""
        
    @rx.var
    def full_raw_path(self) -> str:
        return self.router.page.full_raw_path

    @rx.var
    def page_path(self) -> str:
        return self.router.page.path
    
    @rx.var
    def get_wonbu_no(self) -> str:
        return self.router.page.params.get("wonbu_no", "no data")

    @rx.var
    def get_post_id(self) -> str:
        return self.router.page.params.get("post_id", "no data")
    
    @rx.event
    def load_mra(self):
        file_path = "./uploaded_files/sample/sample_4_os8F3MP0s9.pdf"
        print(file_path)
        with open(file_path, "rb") as file:
            content = file.read()    

        # encode PDF
        self.base64_pdf = base64.b64encode(content).decode("utf-8")


def test_page() -> rx.Component:
    # Welcome Page (Index)
    
    my_child = rx.container(
                rx.el.Embed(
                    height="88vh",
                    width="100%",
                    id="viewer",
                ),
                rx.script(
                    f"""
    const base64String = {TestState.base64_pdf}
    const byteArray = Uint8Array.from(atob(base64String), c => c.charCodeAt(0));
    """
                ),
    rx.script(
        """ 
    const blob = new Blob([byteArray], { type: 'application/pdf' });

    const viewer = document.getElementById('viewer');
    const objectUrl = URL.createObjectURL(blob);

    viewer.setAttribute('src', objectUrl);
    viewer.onload = () => URL.revokeObjectURL(objectUrl);        
        """
    ),
    )
    return dashboard_page(my_child)



