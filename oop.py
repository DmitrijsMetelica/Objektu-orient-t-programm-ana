class Cilvēks:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = None
    def introduce(self):
        print("Mani sauc " + self.name + " man ir", self.age + " gadi ")
        if self.status:
            print("Es esmu no "+ self.status + "šajā ģimenes")

class Gimene:
    def __init__(self, uzvards, status):
        self.uzvards = uzvards
        self.Status = status

    def setStatus(self, kas):
        kas.status = self.status

p1 = Cilvēks("Dmitrijs" , 18 )

s1 = Gimene("Metļica", "cilvēks")

s1.setStatus(p1) 

