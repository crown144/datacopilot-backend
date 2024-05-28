import json
import sqlalchemy
from sqlalchemy import create_engine, MetaData

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123123@localhost/sky_take_out')

# 获取元数据
metadata = MetaData()
metadata.reflect(bind=engine)

# 构建元数据层的字典
metadata_layer = {}
for table_name, table in metadata.tables.items():
    columns_info = []
    for column in table.columns:
        columns_info.append({
            'name': column.name,
            'type': str(column.type),
            'primary_key': column.primary_key
        })
    metadata_layer[table_name] = columns_info

# 将元数据层保存到 JSON 文件
with open('metadata_layer.json', 'w', encoding='utf-8') as file:
    json.dump(metadata_layer, file, ensure_ascii=False, indent=4)

print("元数据已保存到 metadata_layer.json 文件中")
