import requests
import  pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
file = requests.get(url).text
listo = file.split("\n")
list = [item.split(', ') for item in listo if len(item)!= 0]
with open("6.41iris.pkl", "wb") as f:
    pickle.dump(list, f)


with open("6.41iris.pkl", "rb") as f:
    print(pickle.load(f))

