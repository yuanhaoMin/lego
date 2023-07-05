from enum import Enum

EMPTY_OPERATION = "none"
GOTO = "查看/进入/去/跳转到/打开 "
ADD = "添加/新增/增加 "


class FrontendOperation(Enum):
    VISUALIZE_DATA = ("visualizeData", GOTO + "数据大屏")

    VISUALIZE_TRACK = ("visualizeTrack", GOTO + "轨迹大屏")

    MANAGE_ALARM_HISTORY = ("manageAlarmHistory", GOTO + "告警历史管理 功能/界面/列表")

    MANAGE_SMART_INSPECTION = ("manageSmartInspection", GOTO + "智能巡检 功能/界面/列表")

    MANAGE_FENCE_STRATEGY = ("manageFenceStrategy", GOTO + "围栏策略 功能/界面/列表")
    ADD_FENCE_STRATEGY = ("addFenceStrategy", ADD + "围栏策略")

    MANAGE_INSPECTION_STRATEGY = ("manageInspectionStrategy", GOTO + "巡检策略 功能/界面/列表")
    ADD_INSPECTION_STRATEGY = ("addInspectionStrategy", ADD + "巡检策略")

    def __init__(self, function_name: str, description: str):
        self.function_name = function_name
        self.description = description

    @property
    def metadata(self) -> dict:
        return {
            "function_name": self.function_name,
            "parent_operation": EMPTY_OPERATION,
        }

    @classmethod
    def all_function_names(cls) -> list:
        return [operation.function_name for operation in cls]

    @classmethod
    def all_descriptions(cls) -> list:
        return [
            f"{operation.function_name}: {operation.description}" for operation in cls
        ]

    @classmethod
    def all_metadata(cls) -> list:
        return [operation.metadata for operation in cls]

    @classmethod
    def find_by_function_name(cls, function_name: str):
        for operation in cls:
            if operation.function_name == function_name:
                return operation
        return None
