from elasticsearch5 import Elasticsearch  # 使用对应版本的模块中的类

# elasticsearch 集群服务器的地址
ES = [
    '127.0.0.1:9200'
]

# 创建elasticsearch客户端
es = Elasticsearch(
    ES,
    # 启动前嗅探es集群服务器
    sniff_on_start=True,
    # es集群服务器结点连接异常时是否刷新es节点信息
    sniff_on_connection_fail=True,
    # 每60秒刷新节点信息
    sniffer_timeout=60
)


def search():
    search_name = input("请输入要查询的关键词:")

    query = {

        "from": 0,
        "size": 10000,  # from + size must be less than or equal to: [10000]
        "query": {
            "bool": {
                # 匹配标题或作者
                "should": [{"match_phrase": {"title": search_name}}, {"match_phrase": {"authors": search_name}}]
            }
        },
        'sort': [
            {'bookID': 'asc'}
        ],
    }

    ret = es.search(index='books', doc_type='books', body=query)
    rets = ret['hits']['hits']
    for item in rets:
        print(item["_source"]['bookID'], item["_source"]['title'], item["_source"]['authors'],
              item["_source"]['average_rating'], item["_source"]['isbn'], item["_source"]['isbn13'],
              item["_source"]['language_code'], item["_source"]['# num_pages'], item["_source"]['ratings_count'],
              item["_source"]['text_reviews_count'])
        # print(item["_source"])


if __name__ == '__main__':
    search()
