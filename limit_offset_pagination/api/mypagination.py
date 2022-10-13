from rest_framework.pagination import LimitOffsetPagination



class MyLimitOffstPaginatin(LimitOffsetPagination):
   default_limit = 5
   limit_query_param = 'mylimit'
   offset_query_param = 'myoofset'
   max_limit = 6