class student:
    #private
    __totalstudents =100


    # Constructor
    def __init__(self):
        # calling private methods and property
        self.__privatemethod()
        print(self.__totalstudents)


    # private method
    def __privatemethod(self):
        print('It is private method')

    #public method
    def study(self):
        print("it is public method :) ")
    #public variable
    javastudent = 25

stu = student()
stu.study()
print(stu.javastudent)
#print(stu.__totalstudents)
#stu.__privatemethod
print("__________________________________________________")
print("Access private method and property with class name")
print("__________________________________________________")
stu._student__privatemethod()
print(stu._student__totalstudents)

