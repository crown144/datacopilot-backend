import json
import re
from zhipuai import ZhipuAI
from config import api_key

#json_file_path = './metadata_layer.json'

# 定义提示内容
hint = """解释：!!!表示非常重要的提示，你需要仔细阅读并理解提示内容。提示内容中包含了你需要完成的任务的具体要求和相关信息。
            !!!你的任务是接收自然语言查询并生成一个纯粹的 sql语句查询，将生成的sql查询放在'''sql   '''中
          !!!请仔细阅读我提供的元数据字段注意不要出现表名或者字段名错误，这些数据是我提供给你的一定不是你想出来的,给出结果的时候不要给出不存在的表名和字段,
          !!!一定要仔细阅读我提供的ddl
         CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Birthdate DATE,
    Country VARCHAR(100)
);

-- 创建 Books 表
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    AuthorID INT,
    PublishedYear YEAR,
    Genre VARCHAR(100),
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- 创建 Members 表
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    JoinDate DATE NOT NULL
);

-- 创建 Loans 表
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    LoanDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
          !!!如果用户输入查询不在我提供的字段应该不生成sql
          !!!请特别注意是否有大小写和s结尾(例如Users不要错给成user)：
          注意可能是多表查询，根据你的知识进行数据的整合
          !!!一个示例如下
          输入:1. 查询所有书籍及其作者信息：
          输出：'''sql  SELECT Books.Title, Authors.Name AS Author, Books.PublishedYear, Books.Genre
                        FROM Books
                                JOIN Authors ON Books.AuthorID = Authors.AuthorID;'''
          """




class SQLQueryGenerator:
    def __init__(self):
        self.api_key = api_key
        self.client = ZhipuAI(api_key=self.api_key)
        #self.metadata = self.load_metadata(json_file_path)

    # def load_metadata(self, file_path):
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         metadata = json.load(file)
    #     return metadata

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
        response = None
        for attempt in range(3):
            response = self.client.chat.completions.create(
                model="glm-4",
                messages=messages,
            )
            # 使用正则表达式提取 SQL 查询语句
            matches = re.findall(r"```sql(.+?)```", response.choices[0].message.content, re.DOTALL)

            # 如果找到SQL查询语句，则返回
            if matches:
                return matches[0]
        #print(response)
        # 如果三次尝试后仍然没有找到SQL查询语句，则返回空列表
        return matches

if __name__ == "__main__":
    # 实例化类
    sql_generator = SQLQueryGenerator()

    # 用户输入的内容
    user_input = " 查询奇幻类别的所有书籍及其作者信息"

    # 调用函数生成 SQL 查询语句
    sql_queries = sql_generator.generate_sql_query(user_input)

    # 输出提取到的 SQL 查询语句
    print(sql_queries)
