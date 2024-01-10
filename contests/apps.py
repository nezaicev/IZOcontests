from django.apps import AppConfig
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class ContestsConfig(AppConfig):
    name = 'contests'
    verbose_name = 'Заявки на конкурсы'
