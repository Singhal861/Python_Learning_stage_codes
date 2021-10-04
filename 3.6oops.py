class student():
    relation = 90

    def __init__(self, aname, astd, asection, av):
        self.name = aname
        self.std = astd
        self.section = asection
        self.v = av

    def printdetails(self):
        return f"Name is {self.name}. Standard is {self.std} and section is {self.section} and he is {self.v}"

    @classmethod
    def change_relation(cls, new):
        cls.relation = new

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))
        # param = string.split("-")
        # return cls(param[0], param[1], param[2], param[3])

    @staticmethod
    def printonly(string):
        print("This is good" + string)


class Programmer(student):
    no_of_leaves = 34

    def __init__(self, aname, astd, asection, av, coaching):
        super().__init__(aname, astd, asection, av)
        self.name = aname
        self.std = astd
        self.section = asection
        self.v = av
        self.coaching = coaching


# hari = Programmer("Hariom", 16, "D", "yes", 3)
# print(hari.coaching)
akash = student.from_str("Akash-14-b-n")
print(akash.printdetails())
# print(akash.section)

abhishek = student("Abhishek", 12, "A", "yes")
sarthak = student("Sarthak", 13, "A", "Donn't know")
abhishek.printonly("harry")
# print(bhishek.relation)


# print(bhishek.change_relation(89))


# print(abhishek.relation)
# print(abhishek.section)

# akash = student()
# sarthak = student()
#
# abhishek.std = 12
# akash.std = 13
# sarthak.std = 15
# abhishek.section = " A "
# akash.section =" B "
# sarthak.section = "C"
# abhishek.v = " yes"
# akash.v = " no"
# sarthak.v = "N"
# student.relation = "BFF"
# print(abhishek.__dict__)
# # # print(student.__dict__)
# # print(abhishek.relation)
# print(abhishek.printdetails())
