import reflex as rx
from typing import List
import glob
import os
from datetime import datetime
import asyncio
import base64
from pathlib import Path
#
from .. import navigation
#
#            
def create_unique_filename(file_name: str):
    import random
    import string

    ext = file_name.split(".")[-1]
    name = file_name[:-(len(ext)+1)]
    
    random_name = "".join(
        random.choices(
            string.ascii_letters + string.digits, k=10
        )
    )
    return  name + "_" + random_name + "." + ext

class MRAState(rx.State):
    files: List[dict] = [] 
    #
    uploaded_file: str = ""
    uploading: bool = False
    progress: int = 0
    #
    running: bool = False
    _n_tasks: int = 0
    #
    base64_pdf: str = ""
    
    @rx.var
    def wonbu_no_var(self) -> str:
        #print("MRAState wonbu_no var: ",  self.router.page.params.get("wonbu_no", "no data"))
        return self.router.page.params.get("wonbu_no", "none")
    
    @rx.var
    def full_raw_path(self) -> str:
        return self.router.page.full_raw_path
    
    @rx.event
    def load_mra(self):
        #file_path = "./uploaded_files/sample/sample_4_yp5cTN7dAH.pdf"
        wonbu_no = self.router.page.params.get("wonbu_no", "")
        mra_id = self.router.page.params.get("mra_id", "")
        file_path = f"./uploaded_files/mra/{wonbu_no}/{mra_id}.pdf"
        #print(file_path)
        with open(file_path, "rb") as file:
            content = file.read()    

        # encode PDF
        self.base64_pdf = base64.b64encode(content).decode("utf-8")

    @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        
        wonbu_no = self.router.page.params.get("wonbu_no", "")
        # Read the file data
        upload_data = await files[0].read()
        # Get the upload directory (backend path)
        upload_dir = rx.get_upload_dir() / Path(f"mra/{wonbu_no}")
        # Ensure the directory exists
        #print(upload_dir)
        upload_dir.mkdir(parents=True, exist_ok=True)
        # Create unique filename to prevent conflicts
        unique_filename = create_unique_filename(
            files[0].name
        )
        # Create full file path
        file_path = upload_dir / unique_filename
        # Save the file
        with file_path.open("wb") as f:
            f.write(upload_data)
        # Store filename for frontend display
        self.uploaded_file = unique_filename
        
        #print(self.uploaded_file)
        #print(rx.get_upload_url(self.uploaded_file))
        return MRAState.start_running
                       
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
                    return MRAState.initialize
                if not self.running:
                    self._n_tasks -= 1
                    return 

                self.progress += 10

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5) 

    @rx.event
    def start_running(self):
        self.running = True
        return MRAState.extraction_task
        
    @rx.event
    def cancel_running(self):
        self.running = False
        self.progress = 0
        #print("click cancel.")          

    @rx.event
    def cancel_file(self):
        return rx.clear_selected_files("my_upload")
    
    @rx.event
    async def initialize(self):
        self.uploaded_file = ""
        self.uploading = False
        self.progress = 0
        self.running = False
        self._n_tasks = 0
        #rx.clear_selected_files("my_upload")
        yield rx.clear_selected_files("my_upload")
        yield MRAState.load_files
    
    @rx.event
    async def load_files(self):
        #print("hello load_files")
        # set wonbu_no_var
        #yield navigation.NavState.set_wonbu_no_var
        # get wonbu_no
        wonbu_no = self.router.page.params.get("wonbu_no", "")
        # initialize files at startpoint.
        self.files = []
        # 최대 10개 파일 불러오기 (최근순)
        file_paths = glob.glob(f'./uploaded_files/mra/{wonbu_no}/*.pdf')
        file_paths_with_time = list(map(lambda x: (x, os.stat(x).st_mtime), file_paths))
        file_paths_with_time = sorted(file_paths_with_time, key= lambda x: -x[1])[:10]
        file_paths = [f[0] for f in file_paths_with_time]
        #print(file_paths)
        for file_path in file_paths:
            file_info = os.stat(file_path)
            file_fullname = file_path.split("/")[-1] # 확장자 포함 이름
            file_ext = file_fullname.split(".")[-1]
            file_name = file_fullname[:-(len(file_ext)+1)]
            file_datetime = datetime.fromtimestamp(file_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            file_size = str(round(file_info.st_size / (1024 * 1024),1)) + " MB"
            
            self.files.append(
                {
                    "name": file_name,
                    "ext": file_ext,
                    "datetime": file_datetime,
                    "size": file_size,
                }
            )
            

