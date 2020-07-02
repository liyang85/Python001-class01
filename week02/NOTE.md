# 学习笔记（第二周）

- [学习笔记（第二周）](#学习笔记第二周)
  - [使用 PyMySQL 连接 MySQL](#使用-pymysql-连接-mysql)
    - [游标（Cursor）](#游标cursor)

## 使用 PyMySQL 连接 MySQL

```bash
# 安装 PyMySQL

python3 -m pip install pymysql
```

```py
import pymysql

# 建立数据库连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root_123',
    port=3306
)

# 获取游标
cursor = db.cursor()

# 在游标中执行 SQL 语句
cursor.execute('select version();')

# 获取第一条执行结果
db_version = cursor.fetchone()

print('MySQL version: ', db_version)

# cursor.execute('create database test2 character set utf8mb4;')
# cursor.execute('show create database test2;')
# db_info = cursor.fetchone()
# print('Show DB create info: ', db_info)

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()
```

运行上面的代码，结果如下：

```bash
$ python3 pymysql_demo.py
MySQL version:  ('8.0.19',)

# 注意：fetchone() 的返回值是一个元组。
```

### 游标（Cursor）

> 关系数据库中的操作会对整个行集起作用。例如，由 `SELECT` 语句返回的行集，包括满足该语句的 `WHERE` 子句中条件的所有行。这种由语句返回的完整行集称为「结果集」。应用程序，特别是交互式联机应用程序，并不总能将整个结果集作为一个单元来有效地处理。这些应用程序需要一种机制，以便每次处理一行或一部分行。「游标」就是提供这种机制的（对结果集的）一种扩展。
>
> 游标通过以下方式来扩展结果处理：
>
> - 允许定位在结果集的特定行。
> - 从结果集的当前位置检索一行或一部分行。
> - 支持对结果集中当前位置的行进行数据修改。
> - 如果其他用户对显示在结果集中的数据库数据做出了更改，则提供不同级别的可见性支持。
>
> from <https://docs.microsoft.com/zh-cn/sql/relational-databases/cursors?view=sql-server-ver15>
