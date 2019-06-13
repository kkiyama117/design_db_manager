import re

from adapters.mysql import MySQLManager
from models import DB, ColumnType, Column


def run():
    db = DB("test_db", config={"user": "kiyama", "password": "19980117"})
    mm = MySQLManager(db.name, **db.config)
    for table_name in mm.table_names():
        print(table_name)
        y = mm.column_data(table_name)
        for z in y:
            a = column_factory(z)
            print(a.name)
            print(a.__dict__)
        print()


def column_factory(column_data: dict):
    name = column_data['Field']
    value_type_str = column_data['Type']
    collation = column_data['Collation'] if column_data['Collation'] is not 'None' else None  # utf8_general_ci
    can_null = True if column_data['Null'] is 'YES' else False
    is_primary = True if column_data['Key'] is 'YES' else False
    default = column_data['Default']
    extra = column_data['Extra']
    privileges = column_data['Privileges']
    comment = column_data['Comment']
    a = re.match(r'((.+)?\(([0-9]+)\))', value_type_str)
    b = a.group(2)
    c = a.group(3)
    value_type = ColumnType(b, int(c))
    return Column(name=name, value_type=value_type, collation=collation, can_null=can_null, is_primary=is_primary,
                  default=default, privileges=privileges, extra=extra, comment=comment)


if __name__ == '__main__':
    run()
