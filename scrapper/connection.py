from elasticsearch import Elasticsearch


def conn():
    my_connection = Elasticsearch([{'host':'localhost' , 'port':9200}])
    return my_connection