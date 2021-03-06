import time
import uuid

from ..const import object_type_dict
from ..models import Article, Review, Keyword

from django.db import connection


def query_articles(filters, limit=(0, 10)):
    raw_query = """
        select series_id, title, document, publication_at, category, source_url
        from article 
        where 
         {where_clause} 
        order by series_id
        limit {limit}
    """.format(where_clause=" and ".join(
        filter(lambda item: item is not None, [
            '1=1',
            "title like '%%{}%%'".format(filters["title"]) if filters["title"] is not None else None,

            "publication_at between {}".format(" and ".join(
                map(str, filters["publication_at"]))) if filters["publication_at"][0] is not None else None,

            "category='{}'".format(filters["category"]) if filters["category"] is not None else None,
        ])), limit=", ".join(map(str, filters.get("limit", limit))))

    print(raw_query)
    return Article.objects.raw(raw_query=raw_query)


def save_article(title="", document="", publication_at=0, category=0, source_url="", source_type=0, extra=""):
    series_id = uuid.uuid1()

    Article(
        series_id=series_id,
        title=title,
        document=document,
        publication_at=publication_at,
        category=category,
        source_url=source_url,
        source_type=source_type,
        created_at=int(time.time()),
        updated_at=int(time.time()),
        extra=extra
    ).save()

    return series_id, object_type_dict["article"]


def save_review(object_type, object_id, content="", upvote_num=0, publication_at=0, extra=""):
    series_id = uuid.uuid1()

    Review(
        series_id=series_id,
        object_type=object_type,
        object_id=object_id,
        content=content,
        upvote_num=upvote_num,
        publication_at=publication_at,
        created_at=int(time.time()),
        updated_at=int(time.time()),
        extra=extra
    ).save()

    return series_id


def save_keyword(object_type, object_id, content="", article_url="", extra=""):
    series_id = uuid.uuid1()

    Keyword(
        series_id=series_id,
        object_type=object_type,
        object_id=object_id,
        content=content,
        article_url=article_url,
        created_at=int(time.time()),
        updated_at=int(time.time()),
        extra=extra
    ).save()

    return series_id


def query_keyword_by_content(content):
    raw_query = """
        select series_id, object_type, object_id, content, article_url
        from keyword 
        where content='{content}'
    """.format(content=content)

    return Keyword.objects.raw(raw_query=raw_query)


def execute_sql(sql):
    """
    执行原生SQL
    """
    return Keyword.objects.raw(raw_query=sql)
