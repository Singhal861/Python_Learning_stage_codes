import pickle
# to pickle he file
# cars = ["Audi", "Mercides", "Maruti suzuki", "BMW"]
# with open ("Pick.pkl","wb") as f:
#     pickle.dump(cars, f)

# to load the pickle file
with open ("Pick.pkl", "rb") as f:
    print(pickle.load(f))