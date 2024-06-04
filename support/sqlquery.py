# -*- coding: utf-8 -*-
import pymysql

from pathlib import Path
from dotenv import load_dotenv
import os



class DatabaseConnection:
    def __init__(self):
        self.connection = None
        # �������� .env �ļ�·������ȷ��
        env_file_path = 'support/.env'

        # ���� .env �ļ��еĻ�������
        load_dotenv(dotenv_path=env_file_path)

        # ��ȡ����������ֵ
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
        # ɾ��config�е�'db'�����Ա�������ʱ����ѡ���κ����ݿ�
        config_without_db = self.config.copy()
        config_without_db.pop('db', None)
        self.connection = pymysql.connect(**config_without_db)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, sql, database_name=None):
        try:
            # ����ṩ�����ݿ����֣����л���ָ�����ݿ�
            if database_name:
                self.connection.select_db(database_name)

            with self.connection.cursor() as cursor:
                # ִ��SQL��ѯ
                cursor.execute(sql)

                # ��ȡ���в�ѯ���
                results = cursor.fetchall()

                return results
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

# ʹ��ʾ��
if __name__ == "__main__":
    # ���ݿ�������Ϣ�����������ݿ�����

    # �������ݿ�����ʵ��
    db_connection = DatabaseConnection()

    try:
        # ��������
        db_connection.connect()

        # ִ�в�ѯ������ָ�����ݿ����ƣ�
        sql = "SELECT * FROM users"
        database_name = 'test'  # ��ָ̬�������ݿ�����
        results = db_connection.execute_query(sql, database_name=database_name)

        if results:
            # ��ӡ��ѯ���
            for row in results:
                print(row)
    finally:
        # �ر�����
        db_connection.close()
