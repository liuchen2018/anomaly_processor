import numpy as np
import pandas as pd


class DataCleaner(object):

    def __init__(self):
        pass

    @staticmethod
    def data_cleaning(data, normal_limit, index=None):
        """
        数据清洗
        :param data: DataFrame，需要清洗的数据
        :param normal_limit: list[dict{name:name,upper_limit:upper_limit,lower_limit:lower_limit}]，需要清洗字段的上下限
        :param index:str，需要设置为行名称的字段
        :return:DataFrame，清洗后的数据
        """
        if index:
            data.set_index([index], inplace=True)  # 将时间列设置为行名称
        # 将超过正常范围的值，置NaN
        if normal_limit:
            for normal_limit_i in normal_limit:
                if normal_limit_i.get("upper_limit"):
                    data.loc[data[normal_limit_i["name"]] > normal_limit_i.get("upper_limit")] = np.nan
                if normal_limit_i.get("lower_limit"):
                    data.loc[data[normal_limit_i["name"]] < normal_limit_i.get("lower_limit")] = np.nan
        data = data.dropna(axis=0, how='any')  # 将包含NaN的行丢弃
        return data
