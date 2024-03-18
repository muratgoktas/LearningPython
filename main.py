print("Merhaba  KodlamaIo \nSelam")
header = "Taşıt Kredisi"
#yorum satırı
maturity  = 36

print(header,"Vadesi : ",maturity)
monthlyPayment = 120.4
print("Aylık Ödeme: ",monthlyPayment)
loanAmount = 15000
print("Kredi Tutarı :",loanAmount)
# mod operatörü
print(155 % 5)
print(101 % 2)
# mantıksal operatörler
print(1==1) # True
print(1==2) # False
print(1>1)  # False
print(1<=1) # Truse
print(1!=1) # False
print(1!=2) # True

#or - and
print(1 > 2 or 2>-1) #True
print(3!=4 or 1!=1 and 4>3) #True
print(False or False and True) # False
print(True or 5<3 and False) # True
print(True and False or True) # True
print (True or False and False) # True

#Condition   if, else, elseif =elif
#indent :girinti
number1=100
number2=100
if number1>number2 :
    print(number1 ," Büyüktür",number2)
elif number1<number2:
    print(number1 ," Küçüktür",number2)
else:
    print(number1 ," Eşittir",number2)

print("Yukarıdaki Tab boşluğuna indent denir")
