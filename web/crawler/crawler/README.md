# sentiment_analysis_demo

灵感源自
- [http://fsight.qq.com/Game/173#/outline](http://fsight.qq.com/Game/173#/outline)

我们将根据某个关键词，如“[北马 咸猪手](https://www.baidu.com/s?rsv_idx=1&wd=%E5%8C%97%E9%A9%AC+%E5%92%B8%E7%8C%AA%E6%89%8B&usm=1&ie=utf-8&rsv_cq=%E7%83%AD%E7%82%B9&rsv_dl=0_right_fyb_pchot_20811)”，从网络中爬取文章及评论，并对其进行情感分析，以期获取公众对此事件的态度。

## 1. 数据获取

- **关键词**：关键词将从[百度搜索风云榜](http://top.baidu.com/?vit=1&fr=topcategory_c513)中获取。
- **文章及评论来源**：目前，此项目的主要数据来源为[今日头条](https://www.toutiao.com/)。当项目成熟之后，考虑增加其他数据来源，如微信公众号、贴吧、新浪微博、知乎等。

### 1.1 今日头条爬虫

爬虫的入口地址为 [https://www.toutiao.com/search_content/](https://www.toutiao.com/search_content/)。数据爬取的流程如下：

- 首先，使用关键词搜索，批量获取文章地址。
- 然后，对于每一个文章地址爬取文章及评论。

需要注意的是，文章地址和评论内容需要通过API获得，而文章内容则需要爬虫模拟浏览器以获取。

**使用的工具**

- 数据下载：`requests`、`selenium`
- 网页解析：`BeautifulSoup`

**API**

- 获取文章地址 

> 地址 ：[https://www.toutiao.com/search_content/](https://www.toutiao.com/search_content/)
>
> 参数：keyword (关键词)，offset（从第几条新闻开始），count（获取的新闻数目)，format（格式）。

- 获取评论

> 地址：https://www.toutiao.com/api/comment/list/
>
> 参数：group_id（文章的id），item_id（一般与group_id一样），offset（从第几条新闻开始），count（获取的评论数目）

##2. 情感分析

暂时考虑两种情感分析方法。

- CNN文本分类

- 使用情感词的方法

  > 1. 设置初始的种子集合
  > 2. 标负
  > 3. 使用PMI对词汇标极性
  > 4. 极性加权

## 3. 网站界面

### 3.1 数据展示模块

### 源数据展示模块
在这个页面中，我们将展示爬取的数据。主要功能为

- 数据筛选
  - 筛选标签包括：时间、数据来源、情感等
- 数据展示
  - 使用一个列表对文章进行展示，主要内容包括：序号、文章名称、评论数、赞、发表时间等
  - 点击列表项，可以展示文章的具体内容

### 3.2 数据分析模块

数据分析模块的主要功能是根据爬取的数据，对关键词进行情感分析。主要功能为

- 展示关键词（事件）的基本信息
- 展示关键词（事件）的情感分析结果（图表、词云）
  - 口碑指数：正向情感文章数/（正向情感+负向情感）
  - 口碑词：常见情感词
  - 文章数、口碑指数的变化：此事件热度和大众情感的变化趋势
  - 热词:TDIDF权重高的词汇
    - 热词列表
    - 热词声量及其变化