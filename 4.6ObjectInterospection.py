class Electronic_devices():
    motherboard = 1
    # ("""Protected""")
    _circuit = 3
    # private
    __connectivity = "wired"
    def __init__(self, name):
        self.name = name

class Pocket_devices(Electronic_devices):
    gps = 1
    bluetooth = 2
    multimedia = "yes"
    screen = 1
    def __init__(self, name, atype):
        self.name = name
        self.type = atype

class Phone(Pocket_devices):
    touchscreen = 1
    Internet = "Yes"
    processor = 2
    camera = 2+1
    battery = 1
    def __init__(self, name, type, acompany, aprice):
        self.name = name
        self.type = type
        self.company = acompany
        self.price = aprice

speaker = Electronic_devices("Speaker")
watch = Pocket_devices("Smart watch", "band")
phone = Phone("Z3", "Gaming phone", "IQOO", 22300)

# print(type(speaker))
o = "hello lodu"
# print(id(speaker))
# dir provide all function that can be perform on variable o
# print(dir(o))
# print(type("hello lodu"))

import inspect
print(inspect.getmembers(speaker))