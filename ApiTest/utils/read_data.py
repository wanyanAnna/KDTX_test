import yaml




def read_data():
    f = open("../config/data.yaml", encoding="utf8")
    data = yaml.safe_load(f)
    return data

get_data=read_data()