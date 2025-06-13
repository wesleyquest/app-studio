import reflex as rx
import asyncio
#
#
"""
파일 업로드 v1
"""
"""
file upload + extraction(background task)
"""
def create_unique_filename(file_name: str):
    import random
    import string

    name = "".join(file_name.split(".")[:-1])
    ext = file_name.split(".")[-1]
    
    random_name = "".join(
        random.choices(
            string.ascii_letters + string.digits, k=10
        )
    )
    return  name + "_" + random_name + "." + ext

class UploadExample(rx.State):
    uploaded_file: str = ""
    uploading: bool = False
    progress: int = 0
    #
    running: bool = False
    _n_tasks: int = 0

    @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        # Read the file data
        upload_data = await files[0].read()
        # Get the upload directory (backend path)
        upload_dir = rx.get_upload_dir()
        # Ensure the directory exists
        upload_dir.mkdir(parents=True, exist_ok=True)
        # Create unique filename to prevent conflicts
        unique_filename = create_unique_filename(
            files[0].name
        )
        # Create full file path
        file_path = upload_dir / unique_filename
        # Save the file
        #with file_path.open("wb") as f:
        #    f.write(upload_data)
        # Store filename for frontend display
        self.uploaded_file = unique_filename
        
        print(self.uploaded_file)
        return UploadExample.start_running
                       
    @rx.event
    def handle_upload_progress(self, progress: dict):
        self.uploading = True
        self.progress = round(progress["progress"] * 100 / 5)
        if self.progress >= 20: # if self.progress >= 100:
            self.uploading = False

    @rx.event
    def cancel_upload(self):
        self.uploading = False
        self.progress = 0
        self.uploaded_file = ""
        return rx.cancel_upload("my_upload")
    
    @rx.event(background=True)
    async def extraction_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return 

            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
            async with self:
                # Check for stopping conditions inside context
                if self.progress >= 100:
                    self.running = False
                    return UploadExample.initialize
                if not self.running:
                    self._n_tasks -= 1
                    return 

                self.progress += 10

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5) 

    @rx.event
    def start_running(self):
        self.running = True
        return UploadExample.extraction_task
        
    @rx.event
    def cancel_running(self):
        self.running = False
        self.progress = 0
        print("click cancel.")          

    @rx.event
    def cancel_file(self):
        return rx.clear_selected_files("my_upload")
    
    @rx.event
    def initialize(self):
        self.uploaded_file = ""
        self.uploading = False
        self.progress = 0
        self.running = False
        self._n_tasks = 0
        return rx.clear_selected_files("my_upload")


def custom_file_upload() -> rx.Component:
    return rx.upload.root(
    rx.box(
        rx.icon(
            tag="cloud_upload",
            style={
                "width": "3rem",
                "height": "3rem",
                "color": "#2563eb",
                "marginBottom": "0.75rem",
            },
        ),
        rx.hstack(
            rx.text(
                "여기에 파일을 업로드해 주세요",
                size="4",
            ),
        ),
        rx.text(
            "확장자가 PDF(.pdf)인 파일 1개만 업로드 가능",
            color_scheme="red",
            size="3",
            style={
                "marginTop": "0.5rem",
            },
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "1.5rem",
            "textAlign": "center",
        },
    ),
    id="my_upload",
    style={
        # "maxWidth": "24rem",
        #"width": "100%",
        "width": "800px",
        "height": "12rem",
        "borderWidth": "2px",
        "borderStyle": "dashed",
        "borderColor": "#60a5fa",
        "borderRadius": "0.75rem",
        "cursor": "pointer",
        "transitionProperty": "background-color",
        "transitionDuration": "0.2s",
        "transitionTimingFunction": "ease-in-out",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
    },
    # rx.upload.root prop
    max_files=1,
    accept={
        "application/pdf": [".pdf"]
    }
    )


def file_upload_v1() -> rx.Component:
    return rx.vstack(
        rx.cond(
            rx.selected_files("my_upload").length() > 0,
            rx.vstack(
                rx.image(src="/pdf_icon.png", width="40px"),
                rx.foreach(
                    rx.selected_files("my_upload"), rx.text
                ),
            rx.cond(
                UploadExample.uploading | UploadExample.running,
                rx.fragment(),
                rx.hstack(
                    rx.button(
                        "Upload",
                        on_click=UploadExample.handle_upload(
                            rx.upload_files(
                                upload_id="my_upload",
                                on_upload_progress=UploadExample.handle_upload_progress,
                            ),
                        ),
                        size="3",
                    ),
                    rx.button(
                        "Cancel",
                        on_click=UploadExample.cancel_file,
                        size="3",
                        variant="outline",
                    ),
                    align="center",
                    padding_top="10px",
                )
            ),
            style={
                # "maxWidth": "24rem",
                #"width": "100%",
                "width": "800px",
                "height": "12rem",
                "borderWidth": "2px",
                "borderStyle": "dashed",
                "borderColor": "#60a5fa",
                "borderRadius": "0.75rem",
                #"cursor": "pointer",
                "transitionProperty": "background-color",
                "transitionDuration": "0.2s",
                "transitionTimingFunction": "ease-in-out",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
            }                
            ),
            custom_file_upload(),            
        ),
        # extraction
        rx.cond(
            UploadExample.uploading | UploadExample.running,
            rx.progress(value=UploadExample.progress, max=100),
        ),
        rx.cond(
            UploadExample.uploading | UploadExample.running,
            rx.button(
                "Cancel",
                on_click=UploadExample.cancel_running,
            ),
        ),
        align="center",
    )

   
