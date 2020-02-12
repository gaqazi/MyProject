# Method Overloading
class student():
    def stu_detail(self,name=None, age=None):
        if(name!= None and age != None):
            print("name: ",name, " and Age : ", age)
        elif (name == None):
            print("Age is :", age)
        elif (age == None):
            print("Name is : " , name)

    # def demo(self, name):
    #     self.name = name
    #     print(self.name)
    #
    # def demo(self, age):
    #     self.age = age
    #     print(self.age)
    #
    # def demo(self, name, age):
    #     self.name = name
    #     self.age = age
    #     print(self.name, self.age)


stu = student()
stu.stu_detail("zain")
stu.stu_detail(20)
stu.stu_detail("Ali", 23)
# stu.demo("sad")
# stu.demo(26)
# stu.demo("zaid", 16)