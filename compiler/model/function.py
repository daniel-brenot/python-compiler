
from typing import Any, List

from compiler.model.statement import StatementModel


class FunctionParameterModel:
    pass

class FunctionModel:

    parameters: List[FunctionParameterModel]
    """The parameters passed into the function"""

    return_type: Any
    """The return type of the function"""

    statements: List[StatementModel]