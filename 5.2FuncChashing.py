import time
from functools import lru_cache

# @lru_cache(maxsize= 3)
@lru_cache(maxsize= 34)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__== "__main__":
    print("Now running some work")
    some_work(6)
    # some_work(2)
    # some_work(5)
    # some_work(9)
    print("done")
    input()
    some_work(6)
    print("Called again")
