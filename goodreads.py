import requests
import bs4

book_title = []
for i  in range(1,41):
    base_url = 'https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_?page={}'.format(i)
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    for book in soup.select('.bookTitle'):
        book_title.append(book.text)

print(book_title)