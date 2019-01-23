from abc import ABCMeta

import six


class CsvDataRead(six.with_metaclass(ABCMeta, object)):
    data_file_path = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        pass

    def get_url_from_data_file(self, case_id):
        """
        从CSV数据文件根据ID获取URL
        :param id: 调研表ID
        :return: 调研表URL
        """
        # 1. 打开csv文件
        f = open(self.data_file_path, 'r', encoding="utf-8")  # 读模式
        # 2. 遍历数据列表获取ID对应数据
        for line in f.readlines():
            line = line.strip()  # 去掉每行头尾空白
            if not len(line):  # 判断是否是空行
                continue  # 是的话，跳过不处理
            # 根据,分隔每行的数据，获得数据列表
            row_item_list = str(line).split(",")
            # 校验当前ID和数据第一列是否一致
            if str(case_id) == row_item_list[0]:
                # 如果一致，则返回第二列的URL
                return row_item_list[1]
            pass
        return None
