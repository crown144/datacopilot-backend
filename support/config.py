import os

# �������Ļ���������Ϊ ZHIPU_API_KEY
api_key = os.getenv('6f06aa9302291829d66c61aa858fc769.hFekc3Z1G6gAOqnv')

# �����������û�����ã��������ṩһ��Ĭ��ֵ�����׳��쳣
if api_key is None:
    raise ValueError("ZHIPU_API_KEY environment variable is not set")
