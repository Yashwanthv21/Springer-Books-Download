import requests
import pandas as pd

df = pd.read_excel('Springer Ebooks-converted.xlsx', skiprows=1)
# df.head()

for index, row in df.iterrows():
    try:
        book_name = row['Book Title'] + ' ' + row['Author'] + ' ' + str(row['Edition']) + '.pdf'
        book_url = row['OpenURL']

        print(book_url)
        r = requests.get(book_url)
        print(r.url)

        #https://link.springer.com/content/pdf/

        book = r.url.split('/')[-1]
        download_url = 'https://link.springer.com/content/pdf/' + book  + '.pdf'

        print(download_url)

        r = requests.get(download_url, stream=True)
        chunk_size = 200
        with open('books/' + book_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
        print(book_name)
        print("done")
    except Exception as e:
        print("Error:", e, row['OpenURL'])
        pass