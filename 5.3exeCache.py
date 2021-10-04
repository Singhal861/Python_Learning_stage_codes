import  time
from functools import  lru_cache


num = int(input())

@lru_cache(maxsize= num)
def exe(n):
    print("funtion on sleep")
    print("Function start")
    time.sleep(n)
    return n

if __name__== "__main__":
    # print("funtion on sleep")
    exe(6)
    # print("funtion on sleep")
    print("complete")
    print(input("say"))

    exe(6)
