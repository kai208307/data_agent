from dataclasses import dataclass
from pathlib import Path

from omegaconf import OmegaConf

# 引入文件
conf_data = Path(__file__).parents[2] / 'conf' / 'conf_test.yaml'


@dataclass
class MyConfig:
    name: str
    age: int
    sex: str


content = OmegaConf.load(conf_data)
structured = OmegaConf.structured(MyConfig)
print(structured)

merged_data = OmegaConf.merge(structured, content)
print(merged_data, type(merged_data))
user_config: MyConfig = OmegaConf.to_object(merged_data)
print(user_config)
print(user_config.name)
