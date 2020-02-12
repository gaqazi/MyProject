#
#Polymorphism is of two types:
# 1 Compile-time Polymorphism
# 2 Run-time Polymorphism
#Compile-time Polymorphism:
# A compile-time polymorphism also called as static polymorphism which gets resolved during the compilation time of the program. One common example is “method overloading”.
# Let me show you a quick example of the same.
class employee1():
    def name(self):

        print("Harshit is his name")


    def salary(self):
        print("3000 is his salary")


    def age(self):
        print("22 is his age")


class employee2():
    def name(self):

        print("Rahul is his name")


    def salary(self):
        print("4000 is his salary")


    def age(self):
        print("23 is his age")


def func(obj):      #Method Overloading
    obj.name()
    obj.salary()
    obj.age()

obj_emp1 = employee1()
obj_emp2 = employee2()

func(obj_emp1)
func(obj_emp2)

# Explanation:
#
# In the above Program, I have created two classes ’employee1′ and ’employee2′ and created functions for both ‘name’, ‘salary’ and  ‘age’
# and printed the value of the same without taking it from the user.
#
# Now, welcome to the main part where I have created a function with ‘obj’ as the parameter and calling all the three functions i.e. ‘name’, ‘age’ and ‘salary’.
#
# Later, instantiated objects emp_1 and emp_2 against the two classes and simply called the function. Such type is called method overloading
# which allows a class to have more than one method under the same name.