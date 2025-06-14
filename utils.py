import requests

def extract_rutube_id(link):
    """Извлекает ID видео из ссылки Rutube"""
    import re
    match = re.search(r"video/([a-f0-9]+)/", link)
    return match.group(1) if match else None

def get_rutube_thumbnail(video_id):
    """Получает ссылку на превью видео с Rutube API"""
    api_url = f"https://rutube.ru/api/video/{video_id}/thumbnail/"
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("url")  # Вернет ссылку на картинку
    except requests.RequestException as e:
        print(f"Ошибка при получении превью Rutube: {e}")
        return None
