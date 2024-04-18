stringWord = "Hello, My name is Murat GÖKTAŞ. I like  python programming.".split()

print(stringWord)
print(stringWord[::-1])
print(stringWord[0])
print(stringWord[:-1])
print(stringWord[:2:-1])
result= len(stringWord)
print(result)
searchWord = "Murat" in stringWord
print(searchWord)

message = 'Hello There. My name is Murat GÖKTAŞ'.split()
print(message)    # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message[0]) # Hello
names = ['Murat','Melike','Kayra']
for name in names:
   print(name)


#****************************************************************
studentA = ['Kayra','Deniz',2013,[70,60,70]]
studentB = ['Melike','Tuana',2008,[80,80,70]]
studentC = ['Coşkun','Hüseyin',1982,[80,70,90]]
result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
result = f"{studentC[0]} {studentC[1]} {2024 - studentC[2]} yaşında ve not ortalaması {(studentC[3][0] + studentC[3][1] + studentC[3][2])/3}"
print(result)

# result = input("Doğum yılını gir :")
# print(2024-int(result))
# print(type(result))
text=""" Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Molestias unde natus, optio nihil dignissimos, nemo tenetur aliquam molestiae nostrum ea 
similique provident sequi quas necessitatibus fuga amet praesentium repudiandae dolorem!"""

print(text)

firstName ="Murat"
lastName ="GÖKTAŞ"
birthDate=1974
age = 50

print("Adı : {0}, Soyadı :{1}, Yaşım: {3}".format(firstName,lastName,birthDate,age))

#yARDIMCI kAYNAK
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))
# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])
# 3- 'website' içinden com karakterlerini alın.
print(website[22:25:])
lenght = len(website)
print(website[lenght-3:lenght]) # 2. yöntem daha kullanışlı olan
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(f'{course[:14]},{course[-15:]}')
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])
# 6- ifadeyi formatlı şekilde yazdırın.
firstName,middleName,lastName,age,birthDate="Melike","Tuana","GÖKTAŞ",16,2008
print(f'Adı :{firstName} {middleName} Soyadı :{lastName} Yaşı :{age} Doğum Yılı :{birthDate}' ) # f formatlı 1. yöntem
print("Adı : {0} {1} Soyadı :{2} Yaşı : {x} Doğum Tarihi : {y}".format(firstName,middleName,lastName,x=age,y=birthDate)) #2. yöntem
#7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s='Hello world'
print(s)
s= s[:6]+'W'+s[7:]
print(s)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
m='abc'
m=m*3
print(m)
# split methodu
message ="Murat, Melike, Kayra,Ali , Veli ,Recep"
liste =message.split(",")
print(message.split(","))
print(liste[1])
# upper - lower

print(message.upper())
print(message.lower())
for item in liste:
    print(f'{item.upper()} x {item.lower()}')
    print(f'{item.title()} - {item.capitalize()}')

print(liste[1].upper())

message = "Kullanıcının yenilenebilir bir veri öğesinin konumunu bulmak isteyeceği bir durum ortaya çıkabilir".split()
messageEng ="There might arise a situation where the user might want to find out the position of a specific data element in the iterable".split()
print(message)
print(messageEng)
merge = [[message[0],messageEng[6],messageEng[7]],[message[2],message[3],message[4],messageEng[16],messageEng[18],messageEng[19]]]
print(merge)
merge1 =[[message[5],messageEng[13],messageEng[14]],[message[6],messageEng[10],messageEng[11]]]
print(merge1)

# index() ve find() arasındaki tek fark  sonuç dönmezse index() -1 değeri geri dönüyor
# find() ise <ValueError: substring not found> 
# string.index(substr, start, end)
# string.find(substr, start, end)

message = "Kullanıcının yenilenebilir bir veri bir öğesinin konumunu bulmak isteyeceği bir durum ortaya çıkabilir"
myIndex= message.index('bir')
myFind=message.find('bir')
print(f'Index output : {myIndex}')
print(f'Find output : {myFind}')
myIndex = message.index('bir',30,len(message))
print(f'Index output : {myIndex}')
myFind = message.find('bir',30,len(message))
print(f'Find output : {myFind}')
# **************** not found *****
myFind = message.find('OlmayanVeri')
print(f'Find output : {myFind}')
# myIndex = message.index('OlmayanVeri')
# print(f'Index output : {myIndex}')



def append(obje,myIndex,  self) -> str:
   # obje =obje[:startIndex-1]+" "+self+" "+obje[startIndex:]
    return  obje[:myIndex-1]+" "+self+" "+obje[len(self)+myIndex:]
mcs = append(message,0,"Murat Göktaş derki :")
print(message.strip("k"))
s= s[:6]+'W'+s[7:]
print(s.replace(" ","Murat"))
# *********************** memoryview
x = memoryview(b"Hello")

print(x)
#return the Unicode of the first character
print(x[0])
print(chr(x[1]))

# **************************** Python Collections (Arrays)
# Pythonda 4 farklı liste tipi vardır. Bunlar; List=[], Tuple=(), Set ve Dictionary veri tipleridir.

# List, elemanları sıralanabilir, köşeli parantez ile gösterilir [], güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.
myList = [1,'Murat','Göktaş',23.3,'Murat',['a',25,[2,3]]]
print(myList)
print(len(myList))
print(myList[5])
print('1. Elemandan öncekiler :  ', myList[:2])
for value in myList:
    print(f'MyList Elemenı : {value}')
myList = [1,2,3,4,5,6]
print('Ters cevirir: ',myList[: : -1])
myList =[['a','b','c'],['X','XI','XII'],[1,2,3]]
print('1.Listenin 2. elemanı :',myList[1][2]) # Result = XII
print(myList[1:2])
# *********************************Liste Methodları 
# --------append()- ekleme
myList=['Ankara','Bursa','Kocaeli']
print(myList) #Result = ['Ankara','Bursa','Kocaeli']
myList.append("Zonguldak")
print(myList) #Result = ['Ankara','Bursa','Kocaeli','Zonguldak']
#Insert - ekle
myList.insert(1,"Erzurum")
print(myList) #Result = ['Ankara','Erzurum','Bursa','Kocaeli','Zonguldak']
#remove('value')- değerle sil
myList.remove('Bursa')
print(myList) #Result = ['Ankara','Erzurum','Kocaeli','Zonguldak']
#pop(index) -indexle sil
myList.pop(3)
print(myList) #Result = ['Ankara','Erzurum','Kocaeli']
#pop() - sonuncu silinir
myList.pop()
print(myList) #Result = ['Ankara','Erzurum']
#+ -ekle
myList =myList+['Van','İstanbul','Hakkari','Diyarbakır','Kars','Giresun']
print(myList)
#del liste[index] -indexle siler
del myList[4]
print(myList) #Result = ['Ankara', 'Erzurum', 'Van', 'İstanbul', 'Diyarbakır', 'Kars', 'Giresun']
#del liste - tüm listeyi siler
del myList
##print(myList) #Result =  # NameError: name 'list' is not defined
#(+) ekle 
myList=['Ankara', 'Erzurum', 'Van', 'İstanbul', 'Diyarbakır', 'Kars', 'Giresun']
print(myList)
#Liste Kopyalama -Referans Tiptir referans adresini kopyalar
ListI =['a','b','c']
print(ListI) #Result = ['a','b','c']
ListII =[1,2,3]
ListI =ListII 
print(ListI) #Result = [1,2,3]
ListI[1]='Updated'
print(ListII) #Result = [1,'Updated',3]

#.copy() - Referans tiplerde sadece valueları kopyalamakta kullanılır 
aList = ["apple","banana"]
bList = ["grape","cherry"]
aList = bList.copy()
bList[0] = "updated"
print(aList, bList) #Result = ['grape','cherry'] ['updated','cherry']
#.list() .copy() ile aynı işlevi görürür
aList = ["apple","banana"]
bList = ["grape","cherry"]
aList = list(bList)
bList[0] = "updated"
print(aList, bList)   # çıktı: ['grape', 'cherry'] ['updated', 'cherry']

#Liste elemanlarını sıralamak
# .sort() sıralar str ve int ayrı liste olmalıdır.
cList =['d','2','a','4','e','2']
cList.sort()
print(cList) #Result = ['2','2','4','a','d','e']
#.reverse() dersine sıralar
cList=[1,2,3,4,5,6]
cList.reverse()
print(cList) #Result = ['6','5','4','3','2','1']
#Liste Min() Max()
#Min() Max()
cList=[1,2,34,5,64,89,7]
print('Min : ',min(cList))
print('Max : ',max(cList))
cList=['Ali','Ahmet','Aydın','Asım','Alp','Adana','Adam','Ayhan','Alp','Alp']
print(min(cList))
print(max(cList))
#.count() 
print(cList.count('Alp')) #Result = 3
#.clear
print(cList)
cList=cList.clear
print(cList)
# Tuple,parantez ile gösterilir() elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.
# Pythonda tuple listeleri, list' e 
# benzer ancak farkı tuple içindeki elemanlar değiştirilemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.
myTuple =('Kadın','Erkek',41,'Yaşlı','Genç')
print(myTuple)
# Listeye aktarılararak ekleme yapmak
myList =list(myTuple)
myList[2] ='Çocuk'
myTuple =tuple(myList)
print(myTuple)

print(myTuple[0:1])
print(myTuple[:1])
print('(Count) Erkek elemanı var mı ? : ',myTuple.count('Erkek')) # Varsa 1 yoksa 0 
print('Index kaçıncı sırada : ',myTuple.index('Yaşlı'))

myList.reverse
print(myList)


# Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

# Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
a = 2
b = 5
print("YES") if a == b else  print("NO")
#Exmaple *******************************
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#**************************************
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#***************************************
for x in range(6):
  print(x)
#**************************************
def my_function():
  print("Hello from a function")
my_function()
#*************************************
def my_function1(*kids):
  print("The youngest child is " + kids[2])
my_function1('Kayra','222','Melike','Ali')
#***************************************
def my_function3(**kid):
  print("His last name is " + kid["lname"])
#my_function3('lname :selam','Merhaba')
#***************************************
  x = lambda a:a
  print(x)
#***************************************
x = lambda a, b, c : a + b + c
print((x)(5, 6, 2))
#***************************************
x = lambda a : a + 10
print(x(5))
#**************************************
def carp(n):
  return lambda a : a * n
carpan = carp(2)
print(carpan(11))
#**************************************
import numpy as np
myNumpy =dir(np)
print(dir(np))
#*************************************
# # class Person:
   
# #    def __init__ (self, firstName,lastName):
# #       self.firstName = firstName
# #       self.lastName = lastName

# #    def __str__(self):
# #       return f"{self.firstName} {self.lastName}"

# # class Student(Person):
   
# #    def __init__ (self,classNumber,departmen):
# #       self.classNumber =classNumber
# #       self.departmen= departmen
      
# #    def __str__(self):
# #        return f" {self.classNumber}{self.departmen}"
      


# # s1= Student()
# # Student.fullName='Melike'
# # Student.lastName='Tuana'
# # Student('5/A','Kimya')

# # print(s1)
#*****************************************************************************
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def __str__(self) ->str:
    return f"{self.firstname} {self.lastname}"
    #print(self.firstname, self.lastname)



x = Person("Kayra", "Deniz")
print(x)
class Student(Person):
   def value(self) -> str:
     print('Selam')
   
x = Student("Melike", "Tuana")
print(x,x.value())
#********************************************************************************
def carp(n):
  return lambda a : a * n

carpan = carp(2)

print(carpan(11))
#*********************************************************************************
vade=20
print("(1. gösterim) Vade sayıdı :",vade)   
print("(2. gösterim) Vade sayıdı : " +str(vade) )
print("(3. gösterim) Vade sayıdı : {vadesayisi}".format(vadesayisi =vade)) 
print(f"(4. gösterim) Vade sayıdı : {vade}") 
 
# List -Listeler []
print("***************** Listeler [] ****************************")
krediler = ["İhtiyaç Kredisi","Taşıt Kredesi","Araç Kredisi"]
print("len() ile eleman saysı :",len(krediler)) #lenght
krediler.append("Öğrenim Kredisi")
print(".append ile 1 eleman ekleme :",krediler)
krediler.extend(["X Kredisi","Y Kredisi"] )
print(".extend ile 1 den fasla eleman eklenmesi :",krediler)
krediler.pop()
print(".pop() ile en sonuncu elamnın silimesi",krediler)
krediler.remove("X Kredisi")
print(".remove('eleman değeri') eleman silinmesi",krediler)
print("**************************** For *******************")
for i in range(10):
  print(i)

for i in range(3,10):
  print("3' ten başla 9'a kadar yaz:",i)
for i in range(0,51,5):
  print("0'dan başla 50'ye kadar 5'er 5'er yaz:",i)

for kredi in krediler:
  print(kredi)

for i in range(len(krediler)):
  print(krediler[i])
print("**********Reverse tersten yazma***********")
for i in range((len(krediler)-1),-1,-1) :
  print(krediler[i])

#fonksiyonlar defination define tanımlama:

def address():
  address="İzmit/Kocaeli"
  print("Banka Adresi:"+address)

address()
address()

def aritmeticMean(number1,number2,number3):
    print(f"Ortalama : {(number1+number2+number3)/3}")

   
aritmeticMean(10,45,90)

def calculateAndReturn(price,discount):
  return price-discount
print(calculateAndReturn(130,45))
