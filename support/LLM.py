import re
from zhipuai import ZhipuAI
from config import api_key


hint = """解释：!!!表示非常重要的提示，你需要仔细阅读并理解提示内容。提示内容中包含了你需要完成的任务的具体要求和相关信息。
            !!!你的任务是接收自然语言查询并生成一个纯粹的 sql语句查询，将生成的sql查询放在'''sql   '''中
          !!!请仔细阅读以下表结构,是一个ddl语言，给出结果的时候不要给出不存在的表名和字段,
          !!!请特别注意是否有大小写和s结尾(例如Users不要错给成user)：
          CREATE TABLE `Users`(
            `UserID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `Username` VARCHAR(255) NOT NULL,
            `Password` VARCHAR(255) NOT NULL,
            `Email` VARCHAR(255) NOT NULL,
            `Role` ENUM('管理员', '普通用户') NOT NULL
          !!!一个示例如下
          输入:查询用户名为张三的用户信息
          输出：'''sql   SELECT * FROM Users WHERE Username='张三';'''
          !!!你只允许查询数据库名为test的内容
          !!!再强调一次，表名是Users而不是user"""
class SQLQueryGenerator:
    def __init__(self):
        self.api_key =  api_key
        self.client = ZhipuAI(api_key=self.api_key)
    def generate_sql_query(self, user_input):
        # 构造消息列表
        messages = [
            {
                "role": "system",
                "content": hint
            },
            {
                "role": "user",
                "content": user_input
            },
        ]

        # 调用大模型进行转换
        response = self.client.chat.completions.create(
            model="glm-4",  # 使用你需要的模型名称
            messages=messages,
        )

        # 正则表达式模式
        pattern = r"'''sql(.+?)'''"

        # 使用正则表达式提取 SQL 查询语句
        matches = re.findall(pattern, response.choices[0].message.content, re.DOTALL)

        # 返回提取到的 SQL 查询语句
        return matches


if __name__ == "__main__":
    # 实例化类
    sql_generator = SQLQueryGenerator()

    # 用户输入的内容
    user_input = "删除高二三班男生张三的数学成绩"

    # 调用函数生成 SQL 查询语句
    sql_queries = sql_generator.generate_sql_query(user_input)

    # 输出提取到的 SQL 查询语句
    print(sql_queries)
    for sql_query in sql_queries:
        print(sql_query.strip())
