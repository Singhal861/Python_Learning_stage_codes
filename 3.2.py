import time
initial = time.time()

k=0
while k<45:
    print(f"This is Abhishek bhai")
    k += 1
    # time.sleep(1)
print(f"for while loop {time.time() - initial} second")

initial2 = time.time()
for i in range(45):
    print(f"This is Abhishek bhai")
    # time.sleep(1)
print(f"for loop {time.time() - initial2} second")


localtime = time.asctime()
print(localtime)