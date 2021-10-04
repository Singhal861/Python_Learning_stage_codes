class Employee:
    def __init__(self, fname, lname):
        self.name = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
    @property
    # @property is use to convert function call in to direct call
    def email(self):
        if self.name == None or self.lname == None:
            return "Email not set"
        return f"{self.name}.{self.lname}@gamil.com"
    @email.setter
    def email(self,string):
        print("Setting.....")
        names = string.split("@")[0]
        self.name = names.split(".")[0]
        self.lname = names.split(".")[1]
        return
    @email.deleter
    def email(self):
        self.name = None
        self.lname = None

    def explain(self):
        return  f"This employee is {self.name} {self.lname} "

Abhishek = Employee("Abhishek", "Singhal")
Akash = Employee("Akash", "Verma")
print(Abhishek.email)
Abhishek.name = "Bishu"
print(Abhishek.email)
Akash.email = "Chotu.Programmer@gmail.com"
print(Akash.email)
del Akash.email
print(Akash.email)
