import reflex as rx
from typing import List
#
#
APP_LIST=[
    {
        "no": 0, 
        "name": "건강보험 수진내역 추출 및 생성",
        "content": "재해자의 건강보험 내역에서 상병과 연관된 내역을 선택하고 재해조사서 생성",
        "category": "재해조사서",
        "tags": ["AI", "LLM"],
    },
    {
        "no": 1, 
        "name": "의무기록 파일 색인 및 요약",
        "content": "재해자의 의무기록에서 텍스트를 추출하고 상병과 연관된 내용을 색인 및 요약",
        "category": "재해조사서",
        "tags": ["OCR", "AI", "LLM"],
    },
    {
        "no": 2, 
        "name": "요양기간 분석",
        "content": "재해자의 요양기간(요양일수)에 대한 분석 정보 제공",
        "category": "요양기간",
        "tags": ["AI"],
    },
]

CATEGORY_LIST = ["전체", "재해조사서", "요양기간"]

class AppDescription(rx.Model, table=False):
    no: int
    name: str
    content: str
    tags: List[str]