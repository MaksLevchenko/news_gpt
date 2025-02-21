import requests
import validators
from bs4 import BeautifulSoup


headers = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


def get_news(url: str) -> list:
    """Получение новости из ссылки"""

    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.find_all("div", class_="article__text")
    news_text = []
    for i in s:

        news_text.append(i.text.strip().replace("\n", "").strip())
    return news_text[0]


def is_url(link: str) -> bool:
    """Регулярное выражение для проверки формата URL"""
    return validators.url(link)
