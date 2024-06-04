# -*- coding: utf-8 -*-
import pymysql

from pathlib import Path
from dotenv import load_dotenv
import os



class DatabaseConnection:
    def __init__(self):
        self.connection = None
        # 假设您的 .env 文件路径是正确的
        env_file_path = 'support/.env'

        # 加载 .env 文件中的环境变量
        load_dotenv(dotenv_path=env_file_path)

        # 获取环境变量的值
        USER = os.getenv('USER')
        PASSWORD=os.getenv('PASSWORD')
        HOST=os.getenv('HOST')
        PORT=os.getenv('PORT')
        db_config = {
        'host': HOST,
        'user': USER,
        'password': PASSWORD,
        'cursorclass': pymysql.cursors.DictCursor
        }
        self.config = db_config

    def connect(self):
        # 删除config中的'db'键，以便在连接时不会选择任何数据库
        config_without_db = self.config.copy()
        config_without_db.pop('db', None)
        self.connection = pymysql.connect(**config_without_db)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, sql, database_name=None):
        try:
            # 如果提供了数据库名字，则切换到指定数据库
            if database_name:
                self.connection.select_db(database_name)

            with self.connection.cursor() as cursor:
                # 执行SQL查询
                cursor.execute(sql)

                # 获取所有查询结果
                results = cursor.fetchall()

                return results
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

# 使用示例
if __name__ == "__main__":
    # 数据库配置信息（不包含数据库名）

    # 创建数据库连接实例
    db_connection = DatabaseConnection()

    try:
        # 建立连接
        db_connection.connect()

        # 执行查询（可以指定数据库名称）
        sql = "SELECT * FROM users"
        database_name = 'test'  # 动态指定的数据库名称
        results = db_connection.execute_query(sql, database_name=database_name)

        if results:
            # 打印查询结果
            for row in results:
                print(row)
    finally:
        # 关闭连接
        db_connection.close()
