with open("book_urls.txt",'w') as f:
    with open("books.txt") as books:
        for line in books:
            if 'http://' in line:
                f.write(line.split()[-1]+"\n")


