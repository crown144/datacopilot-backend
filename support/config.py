from dotenv import load_dotenv
import os
load_dotenv()
# �������Ļ���������Ϊ ZHIPU_API_KEY
api_key = os.getenv('ZHIPU_API_KEY')

# �����������û�����ã��������ṩһ��Ĭ��ֵ�����׳��쳣
if api_key is None:
    raise ValueError("ZHIPU_API_KEY environment variable is not set")
