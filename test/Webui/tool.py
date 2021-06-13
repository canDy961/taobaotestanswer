import yaml
from os.path import dirname
webui_path=dirname((__file__))
# print(webui_path)
conf_path=webui_path+"/conf.yml"  # 获取conf.yml 文件路径
# print(conf_path)

def readConfig():
      with open(conf_path,'r') as f: # 打开conf.yml文件
           data=yaml.safe_load(f)      # 读取文件内容
           print(data)
      return  data



