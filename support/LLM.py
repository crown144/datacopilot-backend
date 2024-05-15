import re
from zhipuai import ZhipuAI

class SQLQueryGenerator:
    def __init__(self):
        self.api_key = "2fbc8f69a4e07642a2ee340cc6c795e6.KgLRimFsXssv7dyj"
        self.client = ZhipuAI(api_key=self.api_key)

    def generate_sql_query(self, user_input):
        # 构造消息列表
        messages = [
            {
                "role": "system",
                "content": "你的任务是接收自然语言查询并生成一个纯粹的 sql语句查询，将生成的sql查询放在'''sql   '''中以下是你需要参考的表结构：学生表（Student）包含字段学号（student_id），姓名（name），性别（gender），班级（class）；课程表（Course）包含字段课程号（course_id），课程名（course_name），学分（credit）；成绩表（Grade）包含字段学号（student_id），课程号（course_id），成绩（score）。"
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
        pattern = r"```sql(.+?)```"

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
