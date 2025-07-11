import reflex as rx
import pandas as pd
import asyncio
#
from .utils.connections import ygtest_conn
#
#
"""
class HealthRecord(rx.Model, table=False):
    no: int
    #ipsu_ilja: str
    #jaehaegeunroja_rgno: str
    jaehaegeunroja_name: str
    #susin_fg: str
    jinryo_ilja: str
    hospital_name: str
    #hospital_phonenumber: str
    ipwon_ilsu: int
    jusangbyeong_cd: str
    jusangbyeong_name: str
    busangbyeong_cd: str
    busangbyeong_name: str
    #teuksusangbyeong_cd: str
    #yanghanbang_fg: str
    #geupyeo_fg: str
    yeongwan_yn: str
"""
class HRAState(rx.State):
    data: list[dict] = []
    columns: list[str] = []
    header_columns: list[str] = []
    
    selected_rows: list[int] = []
    selected_data: list[dict] = []

    total_items: int
    offset: int = 0
    limit: int = 10
    
    summary: str = ""
    
    tab_value: str = "tab1"
    
    @rx.var
    def wonbu_no_var(self) -> str:
        return self.router.page.params.get("wonbu", "none")
    
    @rx.event
    def change_tab_value(self):
        if self.tab_value == "tab2":
            self.tab_value = "tab1"
        else:
            self.tab_value = "tab2" 

    @rx.event
    async def generate_summary(self):
        self.tab_value = "tab2"
        yield
        await asyncio.sleep(2)
        self.get_selected_data()
        self.summary = "안녕하세요. 요약입니다." + str(self.selected_data)
        yield

    @rx.event
    def reset_summary(self):
        self.summary = ""
        self.tab_value = "tab1"

    @rx.var(cache=True)
    def paginated_data(self) -> list[dict]:
        return self.data[self.offset:self.offset + self.limit]

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (len(self.data) + self.limit - 1) // self.limit

    @rx.event
    def next_page(self):
        if self.offset + self.limit < len(self.data):
            self.offset += self.limit

    @rx.event
    def prev_page(self):
        if self.offset - self.limit >= 0:
            self.offset -= self.limit


    """
    sql query를 사용하여 모든 데이터 로드
    외부 DB 접근
    """
    @rx.event
    def load_data(self):
        # load
        df = pd.read_sql(f"""
        SELECT 
        no, jaehaegeunroja_name, jinryo_ilja, hospital_name, ipwon_ilsu,
        jusangbyeong_cd, jusangbyeong_name, busangbyeong_cd, busangbyeong_name, yeongwan_yn
        FROM hra_sample 
        WHERE jaehaegeunroja_rgno='0003203NNbXF/7u8uAE2Ilz7mMZPw=='
        ORDER BY yeongwan_yn DESC, jinryo_ilja DESC
        """, ygtest_conn)
        #ygtest_conn.close()
        
        # preprocessing : 양쪽 공백 제거
        df[['jaehaegeunroja_name', 'hospital_name', 'jusangbyeong_cd', 'jusangbyeong_name', 'busangbyeong_cd','busangbyeong_name']] = df[['jaehaegeunroja_name', 'hospital_name', 'jusangbyeong_cd', 'jusangbyeong_name', 'busangbyeong_cd','busangbyeong_name']].apply(lambda x: x.str.strip(), axis = 1)
        
        # 선택된 로우 저장 및 뷰에서 제외
        self.selected_rows = list(df[df['yeongwan_yn']=='Y']['no'])
        df = df.drop("yeongwan_yn", axis=1)
        # list 변환 후 저장
        self.columns = ["no", "jaehaegeunroja_name", "jinryo_ilja", "hospital_name", "ipwon_ilsu", "jusangbyeong_cd", "jusangbyeong_name", "busangbyeong_cd", "busangbyeong_name"]
        self.header_columns = ["번호", "재해근로자명", "진료일자", "의료기관명", "입원일수", "주상병코드", "주상병명", "부상병코드", "부상병명"]
        self.data = df.to_dict(orient='records')
        
    @rx.event
    def toggle_row_selection(self, index: int) -> None:
        #print(index)
        #print(self.paginated_data[index])
        id = self.paginated_data[index]['no']
        #print(id)
        if id in self.selected_rows:
            self.selected_rows.remove(id)
        else:
            self.selected_rows.append(id)
        #print(self.selected_rows)

    @rx.event
    def toggle_select_all(self) -> None:
        if len(self.selected_rows) == len(self.data):
            self.selected_rows = []
        else:
            self.selected_rows = list(range(len(self.data)))
        #print(self.selected_rows)

    @rx.event
    def get_selected_data(self) -> None:
        #self.selected_data = [self.data[i] for i in self.selected_rows]
        for d in self.data:
            if d['no'] in self.selected_rows:
                self.selected_data.append(d)

