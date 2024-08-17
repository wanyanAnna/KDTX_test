import configparser
import os
import yaml
import os

##########读取yaml和ini配置文件代码封装
ini_path = "../config/settings.ini"
yaml_path = "../config/data.yaml"


# data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
# ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
# file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "upload.jpeg")


class FileRead:
    def __init__(self):
        self.data_path = 'D:\ApiTest\config\data.yaml'
        self.ini_path = ini_path


    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        # print(data)
        return data

    def read_ini(self):
        # config = configparser.ConfigParser()
        # config.read(self.ini_path, encoding='utf8')
        # return config
        config = configparser.ConfigParser()
        config.read('D:\ApiTest\config\settings.ini')  # 确保路径正确
        # 打印配置文件的所有内容
        for section in config.sections():
            print(f"[{section}]")
            for key, value in config.items(section):
                print(f"{key} = {value}")
        return config

    # def read_file(self):
    #     file = open(self.file_path, 'rb')
    #     return {'file': ('upload.jpeg', file, 'image/jpeg')}


base_data = FileRead()
print(base_data.read_ini())

