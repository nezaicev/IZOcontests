import os
import numpy as np
import requests
from PIL import Image, ImageDraw
from django.conf import settings

POSTER_DIR = 'posters'


def download_poster_video(url_video: str) -> None:
    url_poster = get_url_poster(url_video)
    r = requests.get(url_poster)
    r.raise_for_status()
    with open(
            settings.BASE_DIR / settings.MEDIA_ROOT / POSTER_DIR / 'tmp_poster.jpg',
            'wb+') as image:
        image.write(r.content)
    create_circle_image(settings.BASE_DIR / settings.MEDIA_ROOT / POSTER_DIR / 'tmp_poster.jpg')


def get_url_poster(url: str) -> str:
    url_poster = 'https://img.youtube.com/vi/{}/mqdefault.jpg'
    id_video = url.split('/')[-1]
    return url_poster.format(id_video)


def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    """
    Функция для обрезки изображения по центру.
    """
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def create_circle_image(path_image: str) -> None:
    img = Image.open(path_image).convert("RGB")
    img = crop_center(img, 200, 200)
    npImage = np.array(img)
    h, w = img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    npImage = np.dstack((npImage, npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save(
        settings.BASE_DIR / settings.MEDIA_ROOT / POSTER_DIR / 'tmp_poster.png')
