import json
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from pathlib import Path
from dotenv import load_dotenv
import os

# 假设您的 .env 文件路径是正确的
env_file_path = '.env'
# 加载 .env 文件中的环境变量
load_dotenv(dotenv_path=env_file_path)

# 获取环境变量的值
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')
HOST=os.getenv('HOST')
PORT=os.getenv('PORT')

class DatabaseMetadata:
    def __init__(self, database_name):
        # 创建数据库连接
        self.engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{database_name}')
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    def get_metadata(self):
        # 构建元数据层的字典
        metadata_layer = {}
        for table_name, table in self.metadata.tables.items():
            columns_info = []
            for column in table.columns:
                columns_info.append({
                    'name': column.name,
                    'type': str(column.type),
                    'primary_key': column.primary_key
                })
            metadata_layer[table_name] = columns_info
        return metadata_layer

    def save_metadata_to_json(self, file_path):
        # 将元数据层保存到 JSON 文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.get_metadata(), file, ensure_ascii=False, indent=4)
        print(f"元数据已保存到 {file_path} 文件中")

# 使用示例
if __name__ == "__main__":
    #pass
    db_metadata = DatabaseMetadata('search')
    metadata = db_metadata.get_metadata()
    #保存元数据到 JSON 文件
    db_metadata.save_metadata_to_json('./support/metadata_layer.json')


