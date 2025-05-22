import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/category/books/childrens_11/page-{}.html"
    data = []
    page_num = 1

    while True:
        url = base_url.format(page_num)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')

        books = soup.find_all('article', class_='product_pod')

        # Если книг нет — завершаем цикл
        if not books:
            break

        # Сбор данных
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            rating = book.find('p', class_='star-rating')['class'][1]

            data.append({
                'Title': title,
                'Price': price,
                'Rating': rating
            })

        # Переходим на следующую страницу
        page_num += 1

    # Сохранение в Excel
    df = pd.DataFrame(data)
    df.to_excel("childrens_books.xlsx", index=False)
    print("Результат сохранен в файл childrens_books.xlsx")

# Запуск парсера
scrape_books()



