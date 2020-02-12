class person:
    def __init__(self,mame,age,gendar):
        self.name = mame
        self.age = age
        self.gendar = gendar
    def setdata(self):
        print("i am ", self.name, "and my age is = ", self.age, "years and i am a", self.gendar)



class student(person):
    def __init__(self,mame,age,gendar,subject):
        person.__init__(self,mame,age,gendar)
        self.subject= subject
    def setdata(self):
        print("i am ", self.name, "and my subject is ", self.subject)

s =student("Ali",23,"male","IT")
s.setdata()

s2 =student("Aisha",25,"Female","Math")
s2.setdata()

s3= person("Ali",23,"male")
s3.setdata()
