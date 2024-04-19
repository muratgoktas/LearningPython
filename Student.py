class Student:
    def __str__(self) -> str:
        return self.firstName+" "+self.lastName 
    def firstName(self):
        self.firstName
    def lastName(self):
        self.lastName

class StudentDal:
    def __init__(self) -> None:
        pass
   
    def __str__(self) -> str:
        return self.firstName+" "+lastName # type: ignore
    def Add(self,firstName,lastName):
        students.append ([firstName.title(),lastName.upper()])
    def Delete(self,firstName,lastName):
        if [firstName,lastName] in students: 
            students.remove([firstName,lastName])
        else:
            print (f"{firstName} {lastName} kayıtı bulunamadı... ")
    def Update(self,firstName,lastName):
        myIndex= students.index([firstName,lastName])
        if myIndex != -1:
            fValue =input("Yeni adı giriniz: ")
            lValue =input("Yeni soyadı giriniz:")
            students[myIndex]=([fValue.title(),lValue.upper()])
        else:
            print(f"{firstName} ve {lastName}- böyle bir Kayıt yoktur.")
            


        
students =[Student().firstName(),Student().lastName()]
students[0]=(["Murat","GÖKTAŞ"])
#del students[0]
students.append(["Birgül","ÇETİN"])
students.append(["Melike Tuana","GÖKTAŞ"])
print(len(students))
students.pop()
students.remove(["Murat","GÖKTAŞ"])

students.extend([["Murat","GÖKTAŞ"],["Kayra Deniz","GÖKTAŞ"]])
print(len(students))

for student in students:
    print(student)
students.pop(0)
print("**************************")
#print(students[0])
studentDal =StudentDal()
fName =input("Adınız :")
sName = input("Soyadınız :")
studentDal.Add(fName,sName)
studentDal.Add("Hüseyin","GÖKTAŞ")
studentDal.Add("Semra","GÖKTAŞ")
studentDal.Delete("Hüseyn","GÖKTAŞ")
print(students.count(['Murat','GÖKTAŞ']))
#students[1]=([fName,sName])

for student in students:
    print(student)

#print(students[2][0])
studentDal.Update("Semra","GÖKTAŞ")
print(students)
