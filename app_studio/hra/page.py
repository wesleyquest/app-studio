import reflex as rx
#
from ..ui import dashboard_page
#
#
"""
데이터가 많지 않기 때문에 한번에 state에 로드
in-memory filtering and sorting 방식
"""
class State(rx.State):
    data: list[dict] = [
        {"month": "Jan", "desktop": 186, "mobile": 120, "tablet": 45},
        {"month": "Feb", "desktop": 305, "mobile": 180, "tablet": 60},
        {"month": "Mar", "desktop": 237, "mobile": 200, "tablet": 55},
        {"month": "Apr", "desktop": 73, "mobile": 150, "tablet": 40},
        {"month": "May", "desktop": 209, "mobile": 170, "tablet": 50},
        {"month": "Jun", "desktop": 214, "mobile": 190, "tablet": 70},
        {"month": "Jul", "desktop": 265, "mobile": 210, "tablet": 60},
        {"month": "Aug", "desktop": 312, "mobile": 220, "tablet": 65},
        {"month": "Sep", "desktop": 198, "mobile": 160, "tablet": 48},
        {"month": "Oct", "desktop": 175, "mobile": 155, "tablet": 52},
        {"month": "Nov", "desktop": 190, "mobile": 165, "tablet": 49},
        {"month": "Dec", "desktop": 230, "mobile": 195, "tablet": 58},
    ]

    columns: list[str] = ["month", "desktop", "mobile", "tablet"]
    
    selected_rows: list[int] = []
    selected_data: list[dict] = []

    @rx.event
    def toggle_row_selection(self, index: int) -> None:
        if index in self.selected_rows:
            self.selected_rows.remove(index)
        else:
            self.selected_rows.append(index)
        print(self.selected_rows)

    @rx.event
    def toggle_select_all(self) -> None:
        if len(self.selected_rows) == len(self.data):
            self.selected_rows = []
        else:
            self.selected_rows = list(range(len(self.data)))
        print(self.selected_rows)

    @rx.event
    def get_selected_data(self) -> None:
        self.selected_data = [self.data[i] for i in self.selected_rows]


def table_column(column_name: str):
    return rx.table.column_header_cell(
        rx.text(column_name,
                size="3",
                font_family="NotoSansKR-Bold",
                )
    )

def table_row(data: dict[str, str], columns: list[str], index: int):
    return rx.table.row(
                rx.table.cell(
                    rx.checkbox(
                        checked=rx.cond(
                            State.selected_rows.contains(index), True, False
                        ),
                        on_change=lambda: State.toggle_row_selection(index),
                        size="3",
                        cursor="pointer",
                    )
                ),
                rx.foreach(
                    columns,
                    lambda column: rx.table.cell(rx.text(data[column])),
                ),
                background=rx.cond(
                    State.selected_rows.contains(index), rx.color("indigo", 3), "none"
                ),
                _hover={"bg": rx.color("indigo", 3)},
                white_space="nowrap",
                align="center",
                cursor="pointer",
                on_click=lambda: State.toggle_row_selection(index)
            )

def hra_table(
    data: list[dict] | rx.Var[list[dict]],
    columns: list[str] | rx.Var[list[str]],
):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell(
                    rx.checkbox(
                        checked=rx.cond(
                            State.selected_rows.length() == data.length(), True, False
                        ),
                        on_change=lambda: State.toggle_select_all(),
                        size="3",
                        cursor="pointer",
                    ),
                ),
                rx.foreach(columns, table_column),
                white_space="nowrap",
            ),
        ),
        rx.table.body(
            rx.foreach(
                data,
                lambda data_set, index: table_row(data_set, columns, index),
            ),
        ),
        width="100%",
        variant="ghost",
        max_width="800px",
        #size="1",
    )

def hra_page() -> rx.Component:
    my_child = rx.box(
        rx.box(
            hra_table(State.data, State.columns),
            class_name="w-full h-full flex flex-col items-center justify-center",
        ),
        padding_top="5em",
        padding_left="5em",
    )
    return dashboard_page(my_child)

