
from typing import List
from compiler.model.function import FunctionModel

from compiler.model.trait import TraitModel

class ClassMemberModel:
    pass

class ClassModel:
    """
    This model represents a class in the language
    """

    traits: List[TraitModel]
    """Any traits the class implements"""

    members: dict[str, ClassMemberModel]
    """Any values the class has"""

    methods: dict[str, FunctionModel]
    """Any method that belong to the class"""