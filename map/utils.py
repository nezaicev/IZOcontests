import os
import numpy as np
import requests
from PIL import Image, ImageDraw
from django.conf import settings


def download_poster_video(url_video: str) -> str:
    url_poster = get_url_poster(url_video)
    r = requests.get(url_poster)
    r.raise_for_status()
    path_image=settings.BASE_DIR / settings.MEDIA_ROOT / settings.POSTER_DIR / settings.POSTER_TMP_NAME
    with open(path_image,'wb+') as image:
        image.write(r.content)
    path_image=create_circle_image(path_image)
    if os.path.exists(path_image):
        return path_image


def get_url_poster(url: str) -> str:
    url_poster = settings.YOUTUBE_POSTER
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


def create_circle_image(path_image: str) -> str:
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
    path_image=settings.BASE_DIR / settings.MEDIA_ROOT / settings.POSTER_DIR / settings.POSTER_TMP_NAME.replace(
            'jpg', 'png')
    # Save with alpha
    Image.fromarray(npImage).save(path_image)
    return path_image
