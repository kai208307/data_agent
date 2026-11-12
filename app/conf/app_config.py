from dataclasses import dataclass
from pathlib import Path

from omegaconf import OmegaConf


# 又学会一招，配置文件的配置方式，掌柜智库用的是env，掌柜问数用的是yaml配置！！

@dataclass
class Console:
    enable: bool
    level: str


@dataclass
class File:
    enable: bool
    level: str
    path: str
    rotation: str
    retention: str


@dataclass
class Logging:
    file: File
    console: Console


@dataclass
class AppConfig:
    logging: Logging


# 1. 加载yaml文件得到配置内容
yaml_file_path = Path(__file__).parents[2] / 'conf' / 'app_config.yaml'
yaml_file_content = OmegaConf.load(yaml_file_path)
print(yaml_file_content)

# 2. 加载dataclass对象得到结构
app_config_structed = OmegaConf.structured(AppConfig)
app_config_content = OmegaConf.merge(app_config_structed, yaml_file_content)
print(app_config_content, '合并内容')

# 3. 将内容跟结构合并后，转为dataclass对象，并暴露单例对象，用于获取应用所有配置
app_config_merged_content: AppConfig = OmegaConf.to_object(app_config_content)
print(app_config_merged_content)
print(app_config_merged_content.logging)
