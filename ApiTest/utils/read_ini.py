import configparser
ini_path="../config/settings.ini"
def read_ini():
    config=configparser.ConfigParser()
    config.read(ini_path,encoding="utf-8")
    return config
