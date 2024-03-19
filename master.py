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

message = 'Hello There. My name is Sadık Turan'.split()
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
message ="Murat, Melike, Kayra,ali , veli ,recep"
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
#**************** not found *****
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