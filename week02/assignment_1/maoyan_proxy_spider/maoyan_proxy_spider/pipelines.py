# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymysql

# from maoyan_proxy_spider import settings
#
# db_info = {
#     'host': settings.MYSQL_HOST,
#     'port': settings.MYSQL_PORT,
#     'user': settings.MYSQL_USER,
#     'password': settings.MYSQL_PASSWORD,
#     'db': settings.MYSQL_DB_NAME,
#     'table': settings.MYSQL_TBL_NAME,
# }

db_info = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root_123',
    'db': 'spiders',
    'table': 'maoyan',
}


class MaoyanProxySpiderPipeline:

    def __init__(self):
        self.connection = pymysql.connect(
            host=db_info['host'],
            user=db_info['user'],
            passwd=db_info['password'],
            db=db_info['db'],
            charset='utf8mb4',
        )

        self.cursor = self.connection.cursor()


    def open_spider(self, spider):
        try:
            # with self.cursor as cursor:
            self.cursor.execute(f"drop table if exists {db_info['table']}")

            create_tbl = f" \
                create table {db_info['table']} ( \
                    id int not null primary key auto_increment, \
                    name varchar(30), \
                    category varchar(20), \
                    release_date varchar(10) \
                ) character set utf8mb4 auto_increment 1; "

            self.cursor.execute(create_tbl)

        except Exception as e:
            print(e)


    def process_item(self, item, spider):
        try:
            # with self.cursor as cursor:
            name = item['name']
            category = item['category']
            release_info = item['release_info']
            release_date = release_info[:10]
            values = [(name, category, release_date)]

            self.cursor.executemany(
                'insert into ' + db_info['table'] +
                ' (name, category, release_date) values (%s, %s, %s)', values)

            self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            print(e)

        return item


    def close_spider(self, spider):
        self.connection.close()

