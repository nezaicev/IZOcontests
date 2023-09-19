import requests
from bs4 import BeautifulSoup as bs
from contests.utils import upload_file_by_link
from contests.models import Archive


def get_page_site(url):
    page = requests.get(url)
    soup = bs(page.content, 'lxml')
    return soup


def save_to_archive():
    pass


class ParseDataToArchive:

    def __init__(self, contest_name, year, theme, path_in_container):
        self.contest_name = contest_name
        self.year = year
        self.theme = theme
        self.parse_data = []
        self.container_dir = path_in_container

    def _save_data(self):
        for item in self.parse_data:
            print('initial_upload', item['reg_number'])
            item_db = Archive.objects.create(
                contest_name=self.contest_name,
                year_contest=self.year,
                theme=self.theme,
                fio=item['fio'],
                city=item['city'],
                author_name=item['author_name'],
                age=item['age'],
                reg_number=item['reg_number'],
                publish=True,
                image=upload_file_by_link(item['img'], self.container_dir,
                                          item['img'].split('/')[-1].split('.')[1]),
                rating=item['order']
            )
            item_db.save()
            print(item_db.reg_number, item_db.fio, item_db.image)

    def _parse_page(self, url, start_order_num=0, max_rating=0):
        result = []
        if not start_order_num:
            soup = get_page_site(url)
        else:
            soup = get_page_site('{}/{}/'.format(url, start_order_num))
        labels = soup.find_all('h4', class_='space_top_20')
        reg_numbers = soup.find_all('span', class_='price')
        for n, tag in enumerate(soup.find_all('a', class_='swipebox')):

            if labels[n]:
                label = (labels[n].a.prettify().split('\n'))
                fio = label[3].split(' (')[0].strip()
                city = label[5].strip()
                img_url = (tag['href'])
                author_name = (
                    tag['title'].split(',')[0].replace('"', '').replace('«', '').replace('»',
                                                                                         '')).strip()
                age = label[3].split(' (')[1].split(')')[0]
                result.append({
                    'fio': fio,
                    'img': img_url,
                    'city': city,
                    'author_name': author_name,
                    'age': age,
                    'reg_number': bs(str(reg_numbers[n]), 'html.parser').span.text.split('№')[
                        1].strip(),
                    'order': abs(n - max_rating),
                })
        self.parse_data = result

    def upload_to_archive(self, url, page, max_rating):
        self._parse_page(url, page, max_rating)
        self._save_data()
