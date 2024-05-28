from dotenv import load_dotenv
import os
load_dotenv()
# 假设您的环境变量名为 ZHIPU_API_KEY
api_key = os.getenv('ZHIPU_API_KEY')

# 如果环境变量没有设置，您可以提供一个默认值或者抛出异常
if api_key is None:
    raise ValueError("ZHIPU_API_KEY environment variable is not set")
