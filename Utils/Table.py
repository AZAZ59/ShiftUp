from openpyxl import Workbook


class Table(object):
    def __init__(self, list_of_dicts):
        self.__headers__ = set()
        self.__table__ = self.__set_table__(list_of_dicts)
        self.__excel__ = None

    def __set_table__(self, list_dict):
        for _dict in list_dict:
            self.__headers__ |= set(_dict.keys())
        self.__headers__ = list(self.__headers__)
        table = [self.__headers__]
        for _dict in list_dict:
            table.append([_dict.get(header, None) for header in self.__headers__])
        print(table)
        return table

    def get_table(self):
        return self.__table__

    def to_excel(self):
        if self.__excel__ is None:
            wb = Workbook()
            ws = wb.active
            for row in self.__table__:
                ws.append([str(data) if data is not None else '' for data in row])
            self.__excel__ = wb
        return self.__excel__
