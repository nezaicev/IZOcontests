from django.apps import AppConfig
from rest_framework.pagination import PageNumberPagination


class FrontendConfig(AppConfig):
    name = 'frontend'


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class DesignPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


