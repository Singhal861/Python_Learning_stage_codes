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
    def printdetails(self):
        return f"The Name is {self.name}. type is {self.type}. Company is {self.company}"
    def __add__(self, other):
        return self.price + other.price
    def __truediv__(self, other):
        return self.price / other.price
    def __repr__(self):
        return f"Phone( '{self.name}', '{self.company}', '{self.price}')"
    def __str__(self):
        return  f"The Name is {self.name}. type is {self.type}. Company is {self.company}"
    def __floordiv__(self, other):
        return self.price // other.price
    def __and__(self, other):
        return self.price & other.price
    def __is_not__(self, other):
        return self.price is not other.price
    def __is___(self, other):
        return self.price is other.price

speaker = Electronic_devices("Speaker")
watch = Pocket_devices("Smart watch", "band")
phone1 = Phone("Z3", "Gaming phone", "IQOO", 22300)
phone2 = Phone("A30", "Normal", "Samsung", 14500)

# print(phone.multimedia)
# print(speaker._Electronic_devices__connectivity)
print(phone1.__add__(phone2))