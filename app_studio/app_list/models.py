import reflex as rx
from typing import List
#
#
APP_LIST=[
    {
        "no": 0, 
        "name": "건강보험 내역 추출 요약",
        "content": "재해자의 건강보험 내역에서 상병과 연관된 내역을 선택하고 재해조사서 생성",
        "category": "재해조사서",
        "tags": ["AI", "LLM"],
    },
    {
        "no": 1, 
        "name": "의무기록 파일 보기",
        "content": "재해자의 의무기록에서 텍스트를 추출하고 상병과 연관된 내용을 색인 및 요약",
        "category": "재해조사서",
        "tags": ["OCR", "AI", "LLM"],
    },
    {
        "no": 2, 
        "name": "건강검진 결과 요약",
        "content": "재해발생 이전 5개년 내 건강검진 결과를 재해조사서 형태로 요약",
        "category": "재해조사서",
        "tags": ["AI", "LLM"],
    },
    {
        "no": 3, 
        "name": "재해조사서 검사표 요약 작성",
        "content": "재해조사서 검사표를 기반으로 질환 형태별 재해자의 요약 작성",
        "category": "재해조사서",
        "tags": ["AI", "LLM"],
    },
    {
        "no": 4, 
        "name": "재해자 요양기간 분석",
        "content": "재해자가 신청한 요양기간에 대해 과거 유사재해자의 요양기간 및 AI가 예측한 요양기간과 비교 분석",
        "category": "요양기간",
        "tags": ["AI"],
    },
    {
        "no": 5, 
        "name": "요양기간 분석자료 보기",
        "content": "5개년도 전체 재해자의 요양기간에 대한 분석자료 보기",
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

