def sarcher():
    import time
    # some  4 seconds time consuming task
    book = " this is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book :
            print("your text is in the book")
        else:
            print("your text is not in the book")

search = sarcher()
print('search started')
next(search)
search.send(" harry")
search.close()
# input("press any key")
# search.send("harry and code")
# input("press any key")
# search.send("harry code")
# input("press any key")
# search.send("tis is")
# input("press any key")
# search.send("harre")
# input("press any key")
# search.send("harrd code")
