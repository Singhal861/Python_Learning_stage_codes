def funargs(norm, *args, **kwargs):
    print(norm)
    for item in args:
        print(item)
    print("I would like introduce you from our heroes ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


normal = "I am normal arguments and our students are"
har = ["Abhishek", "Krishnkant",
       "Akash", "Sarthak"]
kw = {"Rohan": "Monitor", "harry": "health instructor",
      "Deepak": "Bihari", "Umesh": "Lodu"}
funargs(normal, *har, **kw)
