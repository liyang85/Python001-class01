# 学习笔记（第一周）

- [学习笔记（第一周）](#学习笔记第一周)
  - [Python 内置功能](#python-内置功能)
    - [常用函数](#常用函数)
      - [`help()`](#help)
      - [`type()`](#type)
      - [`dir()`](#dir)
    - [f-string](#f-string)
    - [yield](#yield)
  - [爬虫方案一：使用第三方库的组合](#爬虫方案一使用第三方库的组合)
    - [requests](#requests)
    - [Beautiful Soup](#beautiful-soup)
      - [搜索文档树：`.find()` and `.find_all()`](#搜索文档树find-and-find_all)
      - [获取属性值：`.get()`](#获取属性值get)
    - [XPath and lxml](#xpath-and-lxml)
    - [pandas](#pandas)
  - [爬虫方案二：使用 Scrapy 爬虫框架](#爬虫方案二使用-scrapy-爬虫框架)
    - [安装 Scrapy](#安装-scrapy)
    - [1. 初始化 Scrapy 项目](#1-初始化-scrapy-项目)
    - [2. 生成一个爬虫](#2-生成一个爬虫)
    - [3. 编辑 `settings.py`](#3-编辑-settingspy)
      - [`USER_AGENT`](#user_agent)
      - [`ITEM_PIPELINES`](#item_pipelines)
    - [4. 编辑 `items.py`](#4-编辑-itemspy)
    - [5. 编辑 `pipelines.py`](#5-编辑-pipelinespy)
    - [6. 编写爬虫逻辑 `douban_movie.py`](#6-编写爬虫逻辑-douban_moviepy)
    - [7. 运行爬虫](#7-运行爬虫)
  - [作业难点](#作业难点)

## Python 内置功能

### 常用函数

#### `help()`

```py
>>> help(type)
```

```txt
Help on class type in module builtins:

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
...
```

```py
>>> help(dir)
```

```txt
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
...
```

#### `type()`

```py
>>> a = 3
>>> type(a)
<class 'int'>

>>> b = 'Hello Python'
>>> type(b)
<class 'str'>
```

#### `dir()`

```py
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

### f-string

f-string 是 Python 3.6 加入的新功能，提供更强大易用的字符串格式化功能，可以完全替代早期的 `%s` 和 `str.format()` 格式化工具。最让我觉得方便的是，**f-string 中可以直接嵌入变量、方法、表达式**，用一对花括号就可以区分。

```py
# f-string 语法示例

print(f'HTTP status code: {response.status_code}')
```

几种格式化方式的详细对比参见 [Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/) 。

> 在冒号（`:`）后面传递一个整数可以让该字段成为最小字符宽度。这在使列对齐时很有用。
>
> ```py
> >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
> >>> for name, phone in table.items():
> ...     print(f'{name:10} ==> {phone:10d}')
> ...
> Sjoerd     ==>       4127
> Jack       ==>       4098
> Dcab       ==>       7678
> ```
>
> from <https://docs.python.org/zh-cn/3.7/tutorial/inputoutput.html#formatted-string-literals>

### yield

单词 yield 的其中一个含义就是「产生（收益）」。在 Python 中，**带有 yield 语句的函数就不再是一个普通的函数，而是一个「生成器」函数**。

根据当前的课程进展，对 yield 的了解如下：

- yield 约等于 return，二者都会返回值。
- yield 的性能（内存占用）优于 return，尤其是在数据量非常大的时候。

两篇教程：

- [Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
- [How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)

## 爬虫方案一：使用第三方库的组合

### requests

> **Requests** is an elegant and simple HTTP library for Python, built for human beings.

requests 库可以用来获取网页的 HTML 源代码，比 Python 内建的 `urllib` 库更容易使用。

- [英文文档（v2.24.0）](https://requests.readthedocs.io/en/master/)

- [中文文档（v2.18.1）](https://requests.readthedocs.io/zh_CN/latest/)

```bash
# 安装 requests

python3 -m pip install requests
```

### Beautiful Soup

> **Beautiful Soup** is a Python library for pulling data out of HTML and XML files.

Beautiful Soup 库用于从 HTML 源代码中提取数据。

- [英文文档（v4.9.0）](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [中文文档（v4.4.0）](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

```bash
# 安装 Beautiful Soup

python3 -m pip install bs4
```

#### 搜索文档树：`.find()` and `.find_all()`

通过 `.find()` 和 `.find_all()` 方法搜索文档树。

```py
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for a_tag in tags.find_all('a',):
        print(a_tag.get('href'))
        print(a_tag.find('span',).text)
```

#### 获取属性值：`.get()`

通过 `tag.get('attr')` 获取 XML 或 HTML 标签的属性的值。

```py
print(a_tag.get('href'))
```

### XPath and lxml

> XPath stands for XML Path Language. It uses a non-XML syntax to provide a flexible way of addressing (pointing to) different parts of an XML document.
>
> from <https://developer.mozilla.org/en-US/docs/Web/XPath>

Beautiful Soup 通过标签及其属性来定位 XML / HTML 文档的不同部分，而 XPath 则是另一种完全不同的方式，但更简单、更高效。

- [XPath 教程](http://www.zvon.org/xxl/XPathTutorial/Output_chi/introduction.html)
- [XPath cheat sheet](https://devhints.io/xpath)

> We won’t cover much of XPath here, but you can read more about [using XPath with Scrapy Selectors here](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors). To learn more about XPath, we recommend [this tutorial to learn XPath through examples](http://zvon.org/comp/r/tut-XPath_1.html), and [this tutorial to learn “how to think in XPath”](http://plasmasturm.org/log/xpath101/).
>
> from <https://docs.scrapy.org/en/latest/intro/tutorial.html#xpath-a-brief-intro>

而想要通过 XPath 来定位 HTML 元素，需要借助 `lxml` 这个库。

> lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
>
> from <https://lxml.de/>

```bash
# 安装 lxml

python3 -m pip install lxml
```

### pandas

> pandas is a fast, powerful, flexible and easy to use open source **data analysis and manipulation tool**, built on top of the Python programming language.
>
> from <https://pandas.pydata.org/>

利用 requests / Beautiful Soup / lxml 等工具下载、提取到需要的信息之后，可能需要把这些信息保存下来，以便进一步分析，此时就需要用到 pandas 库。

```bash
# 安装 pandas

python3 -m pip install pandas
```

## 爬虫方案二：使用 Scrapy 爬虫框架

> Scrapy is a fast high-level web crawling and **web scraping** framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.
>
> from <https://docs.scrapy.org/en/latest/>

Web scraping 可以译为「网页抓取」，Scrapy 就是 Scraping 和 Python 的组合词。

关于 Scrapy 的读音：

> Scrapy (**/ˈskreɪpaɪ/**) is a free and open-source web-crawling framework written in Python.
>
> from <https://www.wikiwand.com/en/Scrapy>

### 安装 Scrapy

```bash
python3 -m pip install scrapy
```

添加 Bash 命令行补全功能：

```bash
# 1. download the script
curl -O 'https://raw.githubusercontent.com/scrapy/scrapy/master/extras/scrapy_bash_completion'

# 2. move the script to the right directory
mv scrapy_bash_completion /usr/local/etc/bash_completion.d/

# 3. activate the script
source /usr/local/etc/bash_completion.d/scrapy_bash_completion
```

完成以上三步之后，再输入 `scrapy startproject` 这样的命令，就可以利用自动补全功能简化输入：`scra <tab> st <tab>`，这里的 `<tab>` 代表键盘上的 TAB 键。

### 1. 初始化 Scrapy 项目

```bash
# 初始化一个项目，项目名称叫做 douban_movie_spider

$ scrapy startproject douban_movie_spider
New Scrapy project 'douban_movie_spider', using template directory '/Users/yangli/.pyenv/versions/3.7.7/lib/python3.7/site-packages/scrapy/templates/project', created in:
    /Users/yangli/geekuniversity_python/playground/douban_movie_spider

You can start your first spider with:
    cd douban_movie_spider
    scrapy genspider example example.com

# 初始化完毕之后，自动创建了同名的 douban_movie_spider 目录
```

初始化其实就是创建一系列文件和目录，具体如下：

```bash
# 末尾有斜线的是目录

$ tree -CF douban_movie_spider/
douban_movie_spider/
├── douban_movie_spider/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── __pycache__/
└── scrapy.cfg

4 directories, 7 files
```

各个文件的用途如下：

- `scrapy.cfg`
  - Scrapy 的配置文件。

- `settings.py`
  - 爬虫的设置文件。

- `items.py`
  - 定义爬取对象的数据结构。

- `pipelines.py`
  - 设置如何保存爬取的数据。

### 2. 生成一个爬虫

可以针对一个或多个域名（domain）生成（generate）一个爬虫，命令如下：

```bash
$ cd douban_movie_spider

$ scrapy genspider douban_movie movie.douban.com
Created spider 'douban_movie' using template 'basic' in module:
  douban_movie_spider.spiders.douban_movie

# 爬虫名称：douban_movie
# 针对域名：movie.douban.com
```

执行 `scrapy genspider` 命令之后，文件系统的变化如下：

```bash
$ tree -cCDF .
.
├── [Jun 28 10:17]  douban_movie_spider/
│   ├── [Jun 28 10:17]  __init__.py
│   ├── [Jun 28 10:17]  items.py
│   ├── [Jun 28 10:17]  middlewares.py
│   ├── [Jun 28 10:17]  pipelines.py
│   ├── [Jun 28 10:17]  settings.py
│   ├── [Jun 28 10:26]  __pycache__/
│   │   ├── [Jun 28 10:26]  __init__.cpython-37.pyc
│   │   └── [Jun 28 10:26]  settings.cpython-37.pyc
│   └── [Jun 28 10:26]  spiders/
│       ├── [Jun 28 10:17]  __init__.py
│       ├── [Jun 28 10:26]  __pycache__/
│       │   └── [Jun 28 10:26]  __init__.cpython-37.pyc
│       └── [Jun 28 10:26]  douban_movie.py
└── [Jun 28 10:17]  scrapy.cfg

4 directories, 11 files
```

从方括号里面的时间戳可以看到，变化（新增）的文件如下：

- 与爬虫同名的 `douban_movie.py`，后续将在这个文件中实现爬虫逻辑。
- 两个 `__pycache__` 目录中的 pyc 文件。

### 3. 编辑 `settings.py`

#### `USER_AGENT`

使用 [fake-useragent 库](https://github.com/hellysmile/fake-useragent) 随机生成 User-Agent。

```bash
# 安装 fake-useragent

python3 -m pip install fake-useragent
```

```py
# Crawl responsibly by identifying yourself (and your website) on the user-agent

# https://github.com/hellysmile/fake-useragent
from fake_useragent import UserAgent
ua = UserAgent()
my_ua = ua.random

USER_AGENT = my_ua
```

#### `ITEM_PIPELINES`

```py
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'douban_movie_spider.pipelines.DoubanMovieSpiderPipeline': 300,
}
```

### 4. 编辑 `items.py`

```py
class DoubanMovieSpiderItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    rating = scrapy.Field()
    summary = scrapy.Field()
```

### 5. 编辑 `pipelines.py`

```py
class DoubanMovieSpiderPipeline:
    def process_item(self, item, spider):
        name = item['name']
        link = item['link']
        output = f'{name}\t\t{link}\n\n'

        with open('./douban_movies.txt', 'a+', encoding='utf-8') as f:
            f.write(output)

        return item
```

### 6. 编写爬虫逻辑 `douban_movie.py`

```py
import scrapy
from bs4 import BeautifulSoup as bs
from douban_movie_spider.items import DoubanMovieSpiderItem


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={ i * 25 }'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = DoubanMovieSpiderItem()
        soup = bs(response.text, 'html.parser')
        file_names = soup.find_all('div', attrs={'class': 'hd'})

        for i in file_names:
            name = i.find('a').find('span').text
            link = i.find('a').get('href')

            item['name'] = name
            item['link'] = link

            # yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
            yield item
```

### 7. 运行爬虫

```bash
scrapy crawl douban_movie
```

输出的日志如下：

```txt
2020-06-28 20:07:27 [scrapy.utils.log] INFO: Scrapy 2.2.0 started (bot: douban_movie_spider)
2020-06-28 20:07:27 [scrapy.utils.log] INFO: Versions: lxml 4.5.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.7 (default, Jun 17 2020, 11:28:02) - [Clang 11.0.3 (clang-1103.0.32.29)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1g  21 Apr 2020), cryptography 2.9.2, Platform Darwin-19.5.0-x86_64-i386-64bit
2020-06-28 20:07:27 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-06-28 20:07:27 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'douban_movie_spider',
 'EDITOR': 'vim',
 'NEWSPIDER_MODULE': 'douban_movie_spider.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['douban_movie_spider.spiders'],
 'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'}
2020-06-28 20:07:27 [scrapy.extensions.telnet] INFO: Telnet Password: d3ce8cad60c4f32f
2020-06-28 20:07:27 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-06-28 20:07:27 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-06-28 20:07:27 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-06-28 20:07:27 [scrapy.middleware] INFO: Enabled item pipelines:
['douban_movie_spider.pipelines.DoubanMovieSpiderPipeline']
2020-06-28 20:07:27 [scrapy.core.engine] INFO: Spider opened
2020-06-28 20:07:27 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-06-28 20:07:27 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-06-28 20:07:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/robots.txt> (referer: None)
2020-06-28 20:07:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/top250?start=0> (referer: None)
2020-06-28 20:07:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.douban.com/top250?start=0>
{'link': 'https://movie.douban.com/subject/1292052/', 'name': '肖申克的救赎'}
2020-06-28 20:07:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/top250?start=200> (referer: None)
2020-06-28 20:07:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.douban.com/top250?start=0>
{'link': 'https://movie.douban.com/subject/1291546/', 'name': '霸王别姬'}
2020-06-28 20:07:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.douban.com/top250?start=0>

...

2020-06-28 20:07:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/top250?start=150> (referer: None)
2020-06-28 20:07:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/top250?start=225> (referer: None)

...

{'link': 'https://movie.douban.com/subject/1291879/', 'name': '罗生门'}
2020-06-28 20:07:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.douban.com/top250?start=200>
{'link': 'https://movie.douban.com/subject/1291844/', 'name': '终结者2：审判日'}
2020-06-28 20:07:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://movie.douban.com/top250?start=200>

...

2020-06-28 20:07:28 [scrapy.core.engine] INFO: Closing spider (finished)
2020-06-28 20:07:28 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 3399,
 'downloader/request_count': 11,
 'downloader/request_method_count/GET': 11,
 'downloader/response_bytes': 126784,
 'downloader/response_count': 11,
 'downloader/response_status_count/200': 11,
 'elapsed_time_seconds': 1.131113,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 6, 28, 12, 7, 28, 891843),
 'item_scraped_count': 250,
 'log_count/DEBUG': 261,
 'log_count/INFO': 10,
 'memusage/max': 53755904,
 'memusage/startup': 53755904,
 'response_received_count': 11,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 10,
 'scheduler/dequeued/memory': 10,
 'scheduler/enqueued': 10,
 'scheduler/enqueued/memory': 10,
 'start_time': datetime.datetime(2020, 6, 28, 12, 7, 27, 760730)}
2020-06-28 20:07:28 [scrapy.core.engine] INFO: Spider closed (finished)
```

以上就是利用 Scrapy 编写爬虫的基本步骤。

## 作业难点

- 猫眼 PC 版网站很容易触发反爬虫限制，必须登录后复制 Cookie 才可以解除限制，但我许久没有登录过猫眼，忘记了密码，在反复认证的过程中被猫眼禁止尝试登录，24 小时后才可以继续尝试，非常麻烦。
  - 解决方法：手机版网站没有设置严厉的反爬虫限制，使用一个移动设备的 User-Agent 之后，不需要登录，就可以相对容易的爬取。

- 使用 Beautiful Soup 或 XPath 搜索文档树特定节点的时候，语法不熟练。
  - 解决方法：①反复学习授课视频；②仔细阅读官方文档和示例代码；③反复尝试。
