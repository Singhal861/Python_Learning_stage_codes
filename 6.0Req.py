import requests

r = requests.get("https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/")
print(r.text)
print(r.status_code)


# url = "https://www.facebook.com/"
# data = {
#     "phone number": 817157667,
#     "password": "Abhishek@01"
# }
# print(requests.post(url=url, data=data))
