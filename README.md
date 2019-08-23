# search_demo
这个项目的数据来源于https://www.kaggle.com/datasets
直接下载csv文件,然后利用logstash采用file的方式导入elasticsearch.(配置文件见logstash.conf).

elasticsearch和logstash要注意版本一致的问题.

利用elasticsearch5包来操作elasticsearch,实现查询功能.
