class employee():

    def __init__(self,name,age,id,salary,msg="object created"):   #//creating a function

        self.name = name  # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
        self.msg= msg
        print(msg)





emp1 = employee("harshit",22,1000,1234) #//creating objects
emp2 = employee("arjun",23,2000,2234)
#print(emp1.name)
print(emp1.__dict__)  #//Prints dictionary

