class Electronic_devices:
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
    def __init__(self, name, type, acompany):
        self.name = name
        self.type = type
        self.company = acompany

speaker = Electronic_devices("Speaker")
watch = Pocket_devices("Smart watch", "band")
phone = Phone("Z3", "Gaming phone", "IQOO")

print(phone.multimedia)
print(phone._circuit)
print(speaker._Electronic_devices__connectivity)

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism