from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class Reviewlistpagination(PageNumberPagination):
    page_size=1
    page_query_param='pa'
    page_size_query_param='record'
    max_page_size=2
    last_page_strings='last'

class Reviewlistlimitoffpag(LimitOffsetPagination):
    default_limit=4
    max_limit=3
    offset_query_param='start'
    limit_query_param='limitsss'

class Reviewlistcursorpag(CursorPagination):
    page_size=5
    ordering='rating'
