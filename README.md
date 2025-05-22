##  Постановка задачи  
Цель проекта — создать парсер, который извлекает данные о книгах из категории "Children's" на сайте [Books to Scrape](http://books.toscrape.com), включая:  
- Название книги  
- Цену  
- Рейтинг  
Проект позволяет автоматически собирать данные с нескольких страниц и сохранять их в формате Excel для дальнейшего анализа.

## Инструкция по сборке и запуску  

### Требования  
- Python 3.x  
- Библиотеки: `requests`, `beautifulsoup4`, `pandas`, `openpyxl`  
### Установка в терминале
```bash
pip install requests beautifulsoup4 pandas openpyxl

```

## Пример результатов работы парсера  

Результаты сохраняются в файл `childrens_books.xlsx` с таблицей вида:

| Title                                          | Price  | Rating    |
|------------------------------------------------|--------|-----------|
| Birdsong: A Story in Pictures                  | £54.64 | Three     |
| The Bear and the Piano                         | £36.89 | One       |
| The Secret of Dreadwillow Carse                | £56.13 | One       |
| Walt Disney's Alice in Wonderland              | £12.96 | Five      |
