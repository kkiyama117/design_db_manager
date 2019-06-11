"""
DOMAIN
"""
from enum import Enum
from typing import List, Optional


class DB:
    def __init__(self):
        self.tables: List[Table] = []
        self.type = None


class Table:
    def __init__(self):
        self.columns: List[Column] = []
        self.status = None


class Column:
    def __init__(self):
        self.name: str = ""
        self.type: Optional[ColumnType] = None
        self.is_null: bool = False
        self.is_primary: bool = False
        self.default: Optional[str] = None
        self.extra: List[ColumnExtra] = []


# Abstract class
# defined for each SQL
class ColumnType:
    def __init__(self, type_name: str, limit: int = 0):
        self.type_name = type_name
        self.limit = limit

    def __eq__(self, other):
        return (self.type_name is other.type_name) and (self.limit is other.limit)


class ColumnExtra(Enum):
    AUTO_INCREMENT = 1
