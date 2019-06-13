"""
DOMAIN
"""
from enum import Enum
from typing import List, Optional


class DB:
    def __init__(self, name: str, kind="MySQL", config: dict = None, tables=None):
        if tables is None:
            tables = []
        self.name = name
        self.tables: List[Table] = tables
        self.kind = kind
        self.config = config


class Table:
    def __init__(self):
        self.columns: List[Column] = []
        self.status = None


class Column:
    def __init__(self, name, value_type, collation, can_null, is_primary, default, extra, privileges, comment):
        self.name: str = name
        self.value_type: Optional[ColumnType] = value_type
        self.collation = collation
        self.can_null: bool = can_null
        self.is_primary: bool = is_primary
        self.default: Optional[str] = default
        self.privileges = privileges
        self.extra: List[ColumnExtra] = extra
        self.comment = comment


# Abstract class
# defined for each SQL
class ColumnType:
    def __init__(self, type_name: str, limit: int = 0):
        self.type_name = type_name
        self.limit = limit

    def __eq__(self, other):
        return (self.type_name is other.type_name) and (self.limit is other.limit)

    def __str__(self):
        if self.limit < 1:
            return self.type_name
        return "{}({})".format(self.type_name, self.limit)


class ColumnExtra(Enum):
    AUTO_INCREMENT = 1
