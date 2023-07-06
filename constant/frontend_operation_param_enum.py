from constant.frontend_operation_enum import FrontendOperation
from constant.prompt import frontend_operation_param_prompt
from enum import Enum


class FrontendOperationParam(Enum):
    SET_ALARM_HISTORY_PARAM = (
        "setAlarmHistoryParam",
        "告警序号 设置 已处理/误报/临时撤防",
        FrontendOperation.MANAGE_ALARM_HISTORY.function_name,
        frontend_operation_param_prompt.SET_ALARM_HISTORY_PARAM,
    )

    SEARCH_SMART_INSPECTION_PARAM = (
        "searchSmartInspectionParam",
        "搜索/查找 巡检 记录",
        FrontendOperation.MANAGE_SMART_INSPECTION.function_name,
        frontend_operation_param_prompt.SEARCH_SMART_INSPECTION_PARAM,
    )

    ADD_FENCE_STRATEGY_PARAM = (
        "addFenceStrategyParam",
        "设置 推送用户, 告警配置, 围栏代码, 有效时间, 开始时间, 结束时间, 策略行为, 告警级别, 策略描述, 围栏策略名称, 关联用户, 重复日期, 工作日",
        FrontendOperation.ADD_FENCE_STRATEGY.function_name,
        frontend_operation_param_prompt.ADD_FENCE_STRATEGY_PARAM,
    )

    ADD_INSPECTION_STRATEGY_PARAM = (
        "addInspectionStrategyParam",
        "设置 巡检策略名称, 是否重复, 有效时间从xx点开始到xx点结束, 停留时间, 是否有序, 选择人员, 选择围栏, 重复日期, 工作日",
        FrontendOperation.ADD_INSPECTION_STRATEGY.function_name,
        frontend_operation_param_prompt.ADD_INSPECTION_STRATEGY_PARAM,
    )

    def __init__(
        self,
        function_name: str,
        description: str,
        parent_operation: str,
        param_prompt: str,
    ):
        self.function_name = function_name
        self.description = description
        self.parent_operation = parent_operation
        self.param_prompt = param_prompt

    @property
    def metadata(self) -> dict:
        return {
            "function_name": self.function_name,
            "parent_operation": self.parent_operation,
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

    @classmethod
    def find_by_parent_operation(cls, parent_operation: str):
        for operation in cls:
            if operation.parent_operation == parent_operation:
                return operation
        return None
