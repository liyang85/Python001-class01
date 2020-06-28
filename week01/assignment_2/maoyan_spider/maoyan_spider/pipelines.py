# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanSpiderPipeline:
    def process_item(self, item, spider):
        # return item

        name = item['name']
        category = item['category']
        release_info = item['release_info']
        release_date = release_info[:10]

        output = f'{name}, "{category}", {release_date}\n'

        with open('./maoyan_10_films.scrapy.csv', 'a+', encoding='utf-8') as f:
            f.write(output)

        return item
