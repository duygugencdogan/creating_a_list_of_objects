#modules
import datetime
from random import randint

an = datetime.datetime.now()

#main class
class Human():
    #constructor
    def __init__(self,name,surname,age,idno,lifetime):
        self.name = name
        self.surname = surname
        self.age = age 
        self.idno = idno
        self.lifetime = lifetime
        
    #functions
    def born(self):
        birthyear = an.year - int(self.age)
        print("{} {} were born in {}".format(self.name,self.surname,birthyear))
    def live(self):
        print("{} {} lives for {} years".format(self.name,self.surname,self.lifetime))
    def death(self):
        birthyear = an.year - int(self.age)
        print("{} {} is dead in {}".format(self.name,self.surname,birthyear + int(self.lifetime)))

#Using inheritance
class Soldier(Human):
    #constructor
    def __init__(self,name,surname,age,idno,lifetime,job):
        self.name = name 
        self.surname = surname
        self.age = age
        self.idno = idno
        self.lifetime = lifetime
        self.job = job  #A new attribute for Soldier
        
    #function
    def live(self):
        print("{} -> {} {} is a {}.".format(self.idno,self.name,self.surname,self.job))


#defining an empty list
myList = list()  

#append objects into the list
for i in range(0,2):
    #creating object
    soldier = Soldier(input("Enter name:"),input("Enter surname:"),input("Enter age:"),input("Enter id number:"),randint(18,120),input("Enter job:"))
    myList.append(soldier)
    soldier.born()
    soldier.live()
    soldier.death()

print(myList)

#we can use like this, if we want to access values of objects..
print(myList[0].name+"-"+myList[0].surname+"-"+myList[0].age+"-"+myList[0].job) 
print(myList[1].name+"-"+myList[1].surname+"-"+myList[1].age+"-"+myList[1].job) 
