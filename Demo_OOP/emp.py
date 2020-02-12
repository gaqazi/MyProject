class Emp:
    name = "WK"
    desigation = "Sales Ex"
    salesOfWeek = 6

    def hasAchivedTarget(self):
        if self.salesOfWeek >= 5:
            print("Target achived")
        else:
            print("Target achived")



empOne = Emp()
empTwo = Emp()
print(empOne.name)
print(empOne.salesOfWeek)
empOne.hasAchivedTarget()


print(empTwo.name)
print(empTwo.name)

empOne.name = "Azmat"
print(empOne.name)
print(empTwo.name)






